# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterativehardthresholding(RPackage):
	"""Iterative Hard Thresholding Extensions to Cyclops

	Fits large-scale regression models with a penalty that 
  restricts the maximum number of non-zero regression coefficients
  to a prespecified value.  While Chu et al (2020) <doi:10.1093/gigascience/giaa044>
  describe the basic algorithm, this package uses Cyclops for an efficient implementation.
	"""
	
	cran = "IterativeHardThresholding" 

	version("1.0.2", md5="a662b94f0d159f0b5954b4c6275f3ca0")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-cyclops@1.3:", type=("build", "run"))
	depends_on("r-parallellogger", type=("build", "run"))
