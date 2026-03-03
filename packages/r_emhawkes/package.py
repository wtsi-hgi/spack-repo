# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmhawkes(RPackage):
	"""Exponential Multivariate Hawkes Model

	Simulate and fitting exponential multivariate Hawkes model. 
    This package simulates a multivariate Hawkes model, introduced by Hawkes (1971) <doi:10.2307/2334319>, with an exponential kernel and fits the parameters from the data. 
    Models with the constant parameters, as well as complex dependent structures, can also be simulated and estimated. 
    The estimation is based on the maximum likelihood method, introduced by introduced by Ozaki (1979) <doi:10.1007/BF02480272>, with 'maxLik' package.
	"""
	
	cran = "emhawkes" 

	version("0.9.7", md5="6f45c216c6460f1d8dbfb40b431699e0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
