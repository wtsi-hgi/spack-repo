# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScqe(RPackage):
	"""Stability Controlled Quasi-Experimentation

	Functions to implement the stability controlled 
    quasi-experiment (SCQE) approach to study the effects of 
    newly adopted treatments that were not assigned at random. This package 
    contains tools to help users avoid making statistical assumptions that rely 
    on infeasible assumptions. Methods developed in Hazlett (2019) 
    <doi:10.1002/sim.8717>.
	"""
	
	cran = "scqe" 

	version("1.0.0", md5="1bb122de74a44624a8bc7d31557e46b4")

	depends_on("r-aer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
