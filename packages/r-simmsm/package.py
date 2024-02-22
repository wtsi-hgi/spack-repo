# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimmsm(RPackage):
	"""Simulation of Event Histories for Multi-State Models

	Simulation of event histories with possibly non-linear baseline hazard rate functions, non-linear (time-varying) covariate effect functions, and dependencies on the past of the history. Random generation of event histories is performed using inversion sampling on the cumulative all-cause hazard rate functions. 
	"""
	
	cran = "simMSM" 

	version("1.1.42", md5="3ecbf73caf64bd97dc2d6bcaacd5b724")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvna", type=("build", "run"))
