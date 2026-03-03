# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgrifeature(RPackage):
	"""Agriculture Image Feature

	Functions to calculate Gray Level Co-occurrence Matrix(GLCM), RGB-based Vegetative Index(RGB VI) and Normalized Difference Vegetation Index(NDVI) family image features. GLCM calculations are based on Haralick (1973) <doi:10.1109/TSMC.1973.4309314>.
	"""
	
	cran = "agrifeature" 

	version("1.0.3", md5="8535e256591c099a2fa0b0bd83ed493e")

