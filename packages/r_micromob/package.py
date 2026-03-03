# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicromob(RPackage):
	"""Discrete Time Simulation of Mosquito-Borne Pathogen Transmission

	Provides a framework based on S3 dispatch for constructing models
  of mosquito-borne pathogen transmission which are constructed from submodels of various
  components (i.e. immature and adult mosquitoes, human populations). A consistent mathematical
  expression for the distribution of bites on hosts means that different models
  (stochastic, deterministic, etc.) can be coherently incorporated and updated
  over a discrete time step.
	"""
	
	homepage = "https://dd-harp.github.io/MicroMoB/"
	cran = "MicroMoB" 

	version("0.1.2", md5="47301fba23dc1d80da0521c2a14f4b56")

	depends_on("r-abind", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
