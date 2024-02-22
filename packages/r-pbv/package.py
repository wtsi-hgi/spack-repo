# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbv(RPackage):
	"""Probabilities for Bivariate Normal Distribution

	
    Computes probabilities of the bivariate normal distribution
    in a vectorized R function (Drezner & Wesolowsky, 1990, 
    <doi:10.1080/00949659008811236>).
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/pbv"
	cran = "pbv" 

	version("0.5-47", md5="f592479b51b50a68d2ab528e739dfa7c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
