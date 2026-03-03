# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsamgp(RPackage):
	"""Bayesian Spectral Analysis Models using Gaussian Process Priors

	Contains functions to perform Bayesian inference
    using a spectral analysis of Gaussian process priors.
    Gaussian processes are represented with a Fourier series 
    based on cosine basis functions. Currently the package
    includes parametric linear models, partial linear additive
    models with/without shape restrictions, generalized linear
    additive models with/without shape restrictions, and  
    density estimation model. To maximize computational 
    efficiency, the actual Markov chain Monte Carlo sampling 
    for each model is done using codes written in FORTRAN 90.
    This software has been developed using funding supported by
    Basic Science Research Program through the National Research
    Foundation of Korea (NRF) funded by the Ministry of Education
    (no. NRF-2016R1D1A1B03932178 and no. NRF-2017R1D1A3B03035235).
	"""
	
	homepage = "http://statlab2.korea.ac.kr/software/bsamgp"
	cran = "bsamGP" 

	version("1.2.5", md5="18a0785b529afb085523a8df623dd03e")
	version("1.2.4", md5="db44909f3d37c4486c531232e8f77014")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
