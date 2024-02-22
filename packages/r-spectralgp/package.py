# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectralgp(RPackage):
	"""Approximate Gaussian Processes Using the Fourier Basis

	Routines for creating, manipulating, and performing 
 Bayesian inference about Gaussian processes in 
 one and two dimensions using the Fourier basis approximation: 
 simulation and plotting of processes, calculation of 
 coefficient variances, calculation of process density, 
 coefficient proposals (for use in MCMC).  It uses R environments to
 store GP objects as references/pointers.
	"""
	
	homepage = "http://www.jstatsoft.org/v19/a2"
	cran = "spectralGP" 

	version("1.3.3", md5="a26d5e517c9ce33575634aaf7731250e")

	depends_on("r@1.9:", type=("build", "run"))
