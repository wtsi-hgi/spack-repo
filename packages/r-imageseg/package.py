# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageseg(RPackage):
	"""Deep Learning Models for Image Segmentation

	A general-purpose workflow for image segmentation using TensorFlow models based on the U-Net architecture by Ronneberger et al. (2015) <arXiv:1505.04597> and the U-Net++ architecture by Zhou et al. (2018) <arXiv:1807.10165>. We provide pre-trained models for assessing canopy density and understory vegetation density from vegetation photos. In addition, the package provides a workflow for easily creating model input and model architectures for general-purpose image segmentation based on grayscale or color images, both for binary and multi-class image segmentation.
	"""
	
	cran = "imageseg" 

	version("0.5.0", md5="03d336e2651a0bf76f3ce22403f732a3")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
