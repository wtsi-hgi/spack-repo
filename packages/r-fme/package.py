# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFme(RPackage):
	"""A Flexible Modelling Environment for Inverse Modelling,
Sensitivity, Identifiability and Monte Carlo Analysis

	Provides functions to help in fitting models to data, to
  perform Monte Carlo, sensitivity and identifiability analysis. It is
  intended to work with models be written as a set of differential
  equations that are solved either by an integration routine from
  package 'deSolve', or a steady-state solver from package
  'rootSolve'. However, the methods can also be used with other types of
  functions.
	"""
	
	homepage = "http://fme.r-forge.r-project.org/"
	cran = "FME" 

	version("1.3.6.3", md5="a69a6c42eca0e6d172b6a60a097afea5")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
