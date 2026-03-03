# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZinarp(RPackage):
	"""Simulate INAR/ZINAR(p) Models and Estimate Its Parameters

	Simulation, exploratory data analysis and Bayesian analysis of the p-order Integer-valued Autoregressive (INAR(p)) and Zero-inflated p-order Integer-valued Autoregressive (ZINAR(p)) processes, as described in Garay et al. (2020) <doi:10.1080/00949655.2020.1754819>. 
	"""
	
	cran = "ZINARp" 

	version("0.1.0", md5="6207efd7cc34ff2e57c48844ee9b80a0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
