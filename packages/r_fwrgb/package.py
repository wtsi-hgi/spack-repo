# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFwrgb(RPackage):
	"""Fresh Weight Determination from Visual Image of the Plant

	Fresh biomass determination is the key to evaluating crop genotypes' response to diverse input and stress conditions and forms the basis for calculating net primary production. However, as conventional phenotyping approaches for measuring fresh biomass is time-consuming, laborious and destructive, image-based phenotyping methods are being widely used now. In the image-based approach, the fresh weight of the above-ground part of the plant depends on the projected area. For determining the projected area, the visual image of the plant is converted into the grayscale image by simply averaging the Red(R), Green (G) and Blue (B) pixel values. Grayscale image is then converted into a binary image using Otsu’s thresholding method Otsu, N. (1979) <doi:10.1109/TSMC.1979.4310076> to separate plant area from the background (image segmentation). The segmentation process was accomplished by selecting the pixels with values over the threshold value belonging to the plant region and other pixels to the background region. The resulting binary image consists of white and black pixels representing the plant and background regions. Finally, the number of pixels inside the plant region was counted and converted to square centimetres (cm2) using the reference object (any object whose actual area is known previously) to get the projected area. After that, the projected area is used as input to the machine learning model (Linear Model, Artificial Neural Network, and Support Vector Regression) to determine the plant's fresh weight.
	"""
	
	cran = "FWRGB" 

	version("0.1.0", md5="b9d96903c93cb9a94ea53c4c35a0e3c7")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
