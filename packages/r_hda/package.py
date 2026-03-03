# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHda(RPackage):
	"""Heteroscedastic Discriminant Analysis

	Functions to perform dimensionality reduction for classification if the covariance matrices of the classes are unequal. 
	"""
	
	cran = "hda" 

	version("0.2-14", md5="05b052e37a2d2051008c1626bd07c8c2")

	depends_on("r-e1071", type=("build", "run"))
