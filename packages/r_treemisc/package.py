# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreemisc(RPackage):
	"""Data Sets and Functions to Accompany "Tree-Based Methods for
Statistical Learning in R"

	Miscellaneous data sets and functions to accompany Greenwell (2022) 
    "Tree-Based Methods for Statistical Learning in R" <doi:10.1201/9781003089032>.
	"""
	
	cran = "treemisc" 

	version("0.0.1", md5="99c883897d11707f1a798f9b15c92b60")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
