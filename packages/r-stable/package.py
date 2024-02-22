# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStable(RPackage):
	"""Probability Functions and Generalized Regression Models for
Stable Distributions

	Density, distribution, quantile and hazard functions of a
    stable variate; generalized regression models for the parameters
    of a stable distribution. See the README for how to make equivalent calls
    to those of 'stabledist' (i.e., Nolan's 0-parameterization and 
    1-parameterization as detailed in Nolan (2020)). 
    See github for Lambert and Lindsey 1999 JRSS-C journal article, 
    which details the parameterization of the Buck (1995) stable.   
    See the Details section of the `?dstable` help file for context and 
    references.
	"""
	
	homepage = "https://www.commanster.eu/rcode.html"
	cran = "stable" 

	version("1.1.6", md5="16a7ec353ed33075f93b03e8c92a296c")

	depends_on("r@1.4:", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
