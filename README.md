Medical Image Analysis

Medical Image Analysis is a Python-based project designed to perform basic analysis tasks on medical images, specifically computed tomography (CT) scans. The project aims to facilitate the processing and analysis of medical images for research, diagnosis, and treatment planning purposes.
Features

    Image Loading: Load CT images and corresponding segmentation images.
    Image Resampling: Resample CT images to an isotropic resolution of 3x3x3mm.
    Maximum Intensity Projection (MIP): Generate MIP images along the coronal and sagittal axes.
    Aorta Volume Calculation: Calculate the volume of the segmented aorta.

Installation

    Clone or download this repository.
    Install the required Python packages listed in the requirements.txt file using pip:

    pip install -r requirements.txt

Usage

    Ensure that the CT image (CT.nii.gz) and segmentation image (segmentation.nii.gz) are available in the project directory.
    Instantiate the MedicalImageAnalyzer class with the file paths of the CT and segmentation images.
    Use the provided methods to perform image loading, resampling, MIP generation, and volume calculation.
    Example usage:
    from medical_image_analyzer import MedicalImageAnalyzer

# Instantiate the MedicalImageAnalyzer class
ct_filename = 'CT.nii.gz'
seg_filename = 'segmentation.nii.gz'
medical_analyzer = MedicalImageAnalyzer(ct_filename, seg_filename)

# Load images
medical_analyzer.load_images()

# Resample CT image
medical_analyzer.resample_image()

# Create MIP images
medical_analyzer.create_mip_images()

# Save MIP images
mip_coronal_filename = 'mip_coronal.png'
mip_sagittal_filename = 'mip_sagittal.png'
medical_analyzer.save_mip_images(mip_coronal_filename, mip_sagittal_filename)

# Calculate aorta volume
voxel_volume = 3.0 * 3.0 * 3.0 / 1000  # Convert mm^3 to ml
aorta_volume_ml = medical_analyzer.calculate_aorta_volume(voxel_volume)
print(f"Volume of segmented aorta: {aorta_volume_ml:.2f} milliliters")

Dependencies

    NumPy
    NiBabel
    SimpleITK
    Pillow

Author

    Muhammad Irfan
    irfanrazzaq961@gmail.com
