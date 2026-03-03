# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcr(RPackage):
	"""Sparse Principal Component Regression

	The sparse principal component regression is computed. The regularization parameters are optimized by cross-validation.
	"""
	
	homepage = "https://doi.org/10.1016/j.csda.2015.03.016"
	cran = "spcr" 

	version("2.1.1", md5="7a744c7ccfb4903fc00bebffca87f505")

