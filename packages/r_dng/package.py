# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDng(RPackage):
	"""Distributions and Gradients

	Provides density, distribution function, quantile function and random
             generation for the split normal and split-t distributions, and computes their
             mean, variance, skewness and kurtosis for the two distributions (Li, F,
             Villani, M. and Kohn, R. (2010) <doi:10.1016/j.jspi.2010.04.031>).
	"""
	
	homepage = "https://github.com/feng-li/dng/"
	cran = "dng" 

	version("0.2.1", md5="e3d6dc8f099e0025c6a6406b8efba3f6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
