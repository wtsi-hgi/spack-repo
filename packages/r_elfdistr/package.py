# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElfdistr(RPackage):
	"""Kumaraswamy Complementary Weibull Geometric (Kw-CWG) Probability
Distribution

	Density, distribution function, quantile function
    and random generation for the Kumaraswamy Complementary Weibull
    Geometric (Kw-CWG) lifetime probability distribution proposed
    in Afify, A.Z. et al (2017) <doi:10.1214/16-BJPS322>.
	"""
	
	homepage = "https://github.com/matheushjs/elfDistr"
	cran = "elfDistr" 

	version("1.0.0", md5="3fd84ea02861862e4a32c72c1c266a5b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
