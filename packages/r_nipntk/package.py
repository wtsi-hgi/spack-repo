# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNipntk(RPackage):
	"""National Information Platforms for Nutrition Anthropometric Data
Toolkit

	An implementation of the National Information Platforms for 
    Nutrition or NiPN's analytic methods for assessing quality of anthropometric 
    datasets that include measurements of weight, height or length, middle upper 
    arm circumference, sex and age. The focus is on anthropometric status but 
    many of the presented methods could be applied to other variables.
	"""
	
	homepage = "https://nutriverse.io/nipnTK/"
	cran = "nipnTK" 

	version("0.1.0", md5="f2357ada9fecf505420699735ab8c928")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bbw", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
