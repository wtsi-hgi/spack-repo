# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmloutliers(RPackage):
	"""Outlier Detection Using Statistical and Machine Learning Methods

	Local Correlation Integral (LOCI) method for outlier identification is implemented here. The LOCI method developed here is invented in Breunig, et al. (2000), see <doi:10.1145/342009.335388>.
	"""
	
	cran = "SMLoutliers" 

	version("0.1", md5="a9be14e88e65836b339c9fb4ab69c5f7")

