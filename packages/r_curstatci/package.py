# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurstatci(RPackage):
	"""Confidence Intervals for the Current Status Model

	Computes the maximum likelihood estimator, the smoothed maximum likelihood
    estimator and pointwise bootstrap confidence intervals for the distribution 
    function under current status data. 
    Groeneboom and Hendrickx (2017) <doi:10.1214/17-EJS1345>.
	"""
	
	homepage = "https://github.com/kimhendrickx/curstatCI"
	cran = "curstatCI" 

	version("0.1.1", md5="241228c6db3c083a974c73e17bcb47f6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
