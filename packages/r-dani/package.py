# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDani(RPackage):
	"""Design and Analysis of Non-Inferiority Trials

	Provides tools to help the design and analysis of resilient non-inferiority trials. These include functions for sample size 
 calculations and analyses of trials, with either a risk difference, risk ratio or arc-sine difference margin, and a function to run simulations to 
 design a trial with the methods described in Quartagno et al. (2019) <arXiv:1905.00241>.  
	"""
	
	cran = "dani" 

	version("0.1-1", md5="679d33c561e7b9cf054ef2ac805129ef")

	depends_on("r-epi", type=("build", "run"))
