# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKfas(RPackage):
	"""Kalman Filter and Smoother for Exponential Family State Space
Models

	State space modelling is an efficient and flexible framework for 
    statistical inference of a broad class of time series and other data. KFAS 
    includes computationally efficient functions for Kalman filtering, smoothing, 
    forecasting, and simulation of multivariate exponential family state space models, 
    with observations from Gaussian, Poisson, binomial, negative binomial, and gamma 
    distributions. See the paper by Helske (2017) <doi:10.18637/jss.v078.i10> for details.
	"""
	
	homepage = "https://github.com/helske/KFAS"
	cran = "KFAS" 

	version("1.5.1", md5="5b991118dd274ccf5d8139b1af623b68")

	depends_on("r@3.1:", type=("build", "run"))
