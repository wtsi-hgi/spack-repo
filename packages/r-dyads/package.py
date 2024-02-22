# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyads(RPackage):
	"""Dyadic Network Analysis

	Contains functions for the MCMC simulation of dyadic network models j2 (Zijlstra, 2017, <doi:10.1080/0022250X.2017.1387858>) and p2 (Van Duijn, Snijders & Zijlstra, 2004, <doi: 10.1046/j.0039-0402.2003.00258.x>), the multilevel p2 model (Zijlstra, Van Duijn & Snijders (2009) <doi: 10.1348/000711007X255336>), and the bidirectional (multilevel) counterpart of the the multilevel p2 model as described in Zijlstra, Van Duijn & Snijders (2009) <doi: 10.1348/000711007X255336>, the (multilevel) b2 model. 
	"""
	
	cran = "dyads" 

	version("1.2.1", md5="ae91390bdde9a62d6688414d662821d5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cholwishart", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppziggurat", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
