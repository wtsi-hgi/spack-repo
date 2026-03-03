# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlcmtextures(RPackage):
	"""GLCM Textures of Raster Layers

	Calculates grey level co-occurrence matrix (GLCM) based texture measures (Hall-Beyer (2017) <https://prism.ucalgary.ca/bitstream/handle/1880/51900/texture%20tutorial%20v%203_0%20180206.pdf>; Haralick et al. (1973) <doi:10.1109/TSMC.1973.4309314>) of raster layers using a sliding rectangular window. It also includes functions to quantize a raster into grey levels as well as tabulate a glcm and calculate glcm texture metrics for a matrix.
	"""
	
	homepage = "https://ailich.github.io/GLCMTextures/"
	cran = "GLCMTextures" 

	version("0.4.1", md5="959186a59c683c26d48ab9d7e8314ad9")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
