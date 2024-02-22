# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharpdata(RPackage):
	"""Data Sharpening

	Functions and data sets inspired by data sharpening -
             data perturbation to achieve improved performance in
             nonparametric estimation, as described in Choi, E., Hall, P.
             and Rousson, V. (2000).  
             Capabilities for enhanced local linear regression function
             and derivative estimation are included, as well as an
             asymptotically correct iterated data sharpening estimator
             for any degree of local polynomial regression estimation.
             A cross-validation-based bandwidth selector is included which,
             in concert with the iterated sharpener, will often provide
             superior performance, according to a median integrated squared
             error criterion.  Sample data sets are provided to illustrate
             function usage.
	"""
	
	cran = "sharpData" 

	version("1.4", md5="6a9dbd6b1725474716dcd96da3f4efac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
