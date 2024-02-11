import numpy as np
import nibabel as nib
import SimpleITK as sitk
from PIL import Image


class MedicalImageAnalyzer:
    def __init__(self, ct_filename, seg_filename):
        self.ct_filename = ct_filename
        self.seg_filename = seg_filename

    def load_images(self):
        self.ct_img = nib.load(self.ct_filename)
        self.seg_img = nib.load(self.seg_filename)

    def resample_image(self, spacing=(3.0, 3.0, 3.0)):
        resampler = sitk.ResampleImageFilter()
        resampler.SetOutputSpacing(spacing)
        resampler.SetSize(self.ct_img.shape)

        # Extract direction cosines from affine matrix
        direction_cosines = [self.ct_img.affine[i, j] for i in range(3) for j in range(3)]
        resampler.SetOutputDirection(direction_cosines)

        resampler.SetOutputOrigin(self.ct_img.affine[:3, 3])
        self.resampled_ct = resampler.Execute(sitk.GetImageFromArray(self.ct_img.get_fdata()))
        self.resampled_ct = sitk.GetArrayFromImage(self.resampled_ct)

    def create_mip_images(self):
        if isinstance(self.resampled_ct, np.ndarray):
            print("Resampled CT shape:", self.resampled_ct.shape)
        else:
            print("Resampled CT is not a NumPy array")
        mip_coronal = np.max(self.resampled_ct, axis=2)  # Compute maximum along the axial axis (0-based indexing)
        mip_sagittal = np.max(self.resampled_ct, axis=0)  # Compute maximum along the sagittal axis
        self.mip_coronal_img = Image.fromarray((mip_coronal * 255).astype(np.uint8))
        self.mip_sagittal_img = Image.fromarray((mip_sagittal * 255).astype(np.uint8))

    def save_mip_images(self, coronal_filename, sagittal_filename, dpi=400):
        self.mip_coronal_img.save(coronal_filename, dpi=(dpi, dpi))
        self.mip_sagittal_img.save(sagittal_filename, dpi=(dpi, dpi))

    def calculate_aorta_volume(self, voxel_volume):
        seg_data = self.seg_img.get_fdata()
        self.aorta_volume_ml = np.sum(seg_data) * voxel_volume / 1000  # Convert mm^3 to ml
        return self.aorta_volume_ml


def main():
    ct_filename = 'CT.nii.gz'
    seg_filename = 'segmentation.nii.gz'
    mip_coronal_filename = 'mip_coronal.png'
    mip_sagittal_filename = 'mip_sagittal.png'

    medical_analyzer = MedicalImageAnalyzer(ct_filename, seg_filename)
    print("analysing the image")
    medical_analyzer.load_images()
    medical_analyzer.resample_image()
    medical_analyzer.create_mip_images()
    medical_analyzer.save_mip_images(mip_coronal_filename, mip_sagittal_filename)

    voxel_volume = np.prod((3.0, 3.0, 3.0)) / 1000  # Convert mm^3 to ml
    aorta_volume_ml = medical_analyzer.calculate_aorta_volume(voxel_volume)
    print(f"Volume of segmented aorta: {aorta_volume_ml:.2f} milliliters")


if __name__ == "__main__":
    main()
