# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchthem(RPackage):
	"""Matching and Weighting Multiply Imputed Datasets

	Provides essential tools for the pre-processing techniques of matching and weighting multiply imputed datasets. The package includes functions for matching within and across multiply imputed datasets using various methods, estimating weights for units in the imputed datasets using multiple weighting methods, calculating causal effect estimates in each matched or weighted dataset using parametric or non-parametric statistical models, and pooling the resulting estimates according to Rubin's rules (please see <https://journal.r-project.org/archive/2021/RJ-2021-073/> for more details).
	"""
	
	homepage = "https://github.com/FarhadPishgar/MatchThem"
	cran = "MatchThem" 

	version("1.1.0", md5="7cf21fd7a24ae067ade47454c3d0b7e5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matchit@4:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-weightit", type=("build", "run"))
