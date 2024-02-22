# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisdoublesamp(RPackage):
	"""Confidence Intervals with Poisson Double Sampling

	Functions to create confidence intervals for ratios of Poisson
    rates under misclassification using double sampling. Implementations of the 
    methods described in Kahle, D., P. Young, B. Greer, and D. Young (2016). 
    "Confidence Intervals for the Ratio of Two Poisson Rates Under One-Way 
    Differential Misclassification Using Double Sampling." Computational 
    Statistics & Data Analysis, 95:122–132.
	"""
	
	homepage = "https://github.com/dkahle/poisDoubleSamp"
	cran = "poisDoubleSamp" 

	version("1.1.1", md5="e3555fc0f98312c07635776df30e0a4c")

	depends_on("r-rcpp", type=("build", "run"))
