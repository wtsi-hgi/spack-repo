# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSi(RPackage):
	"""Stochastic Integrating

	An implementation of four stochastic methods of integrating in R, including:
    1. Stochastic Point Method (or Monte Carlo Method); 
    2. Mean Value Method; 
    3. Important Sampling Method; 
    4. Stratified Sampling Method.
    It can be used to estimate one-dimension or multi-dimension integration by Monte Carlo methods. And the estimated variance (precision) is given.
    Reference: Caflisch, R. E. (1998) <doi:10.1017/S0962492900002804>.
	"""
	
	cran = "SI" 

	version("0.2.0", md5="8e0d1bb5eb5ced45c5f2c9415a5d14ed")

	depends_on("r@3.0.1:", type=("build", "run"))
