# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummclust(RPackage):
	"""Module to Compute Influence and Leverage Statistics for
Regression Models with Clustered Errors

	Module to compute cluster specific information for regression models
        with clustered errors, including leverage and influence statistics. 
        Models of type 'lm' and 'fixest'(from the 'stats' and 'fixest' packages)
        are supported. 'summclust' implements similar features as the 
        user-written 'summclust.ado' Stata module (MacKinnon, Nielsen & Webb, 2022; 
        <arXiv:2205.03288v1>).
	"""
	
	homepage = "https://s3alfisc.github.io/summclust/"
	cran = "summclust" 

	version("0.7.2", md5="6768336fa9b86788b4ee01042c0de6f8")

	depends_on("r-dreamerr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
