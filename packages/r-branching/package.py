# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBranching(RPackage):
	"""Simulation and Estimation for Branching Processes

	Simulation and parameter estimation of multitype Bienayme - Galton - Watson processes.
	"""
	
	cran = "Branching" 

	version("0.9.7", md5="52c49718b9e3e11673dbfe95707419d6")

