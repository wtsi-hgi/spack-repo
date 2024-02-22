# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdp2(RPackage):
	"""Bayesian Adaptive Designs for Phase II Trials with Binary
Endpoint

	Tools and workflow to choose design parameters in Bayesian adaptive single-arm phase II trial designs with binary endpoint (response, success) with possible stopping for efficacy and futility at interim analyses. Also contains routines to determine and visualize operating characteristics. See Kopp-Schneider et al. (2018) <doi:10.1002/bimj.201700209>. 
	"""
	
	cran = "BDP2" 

	version("0.1.3", md5="ac14350045b5b8bbb0d1374e88900b4f", url="https://cran.r-project.org/src/contrib/BDP2_0.1.3.tar.gz")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
