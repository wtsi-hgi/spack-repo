# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimvitd(RPackage):
	"""Simulation Tools for Planning Vitamin D Studies

	Simulation tools for planning Vitamin D studies. Individual vitamin D status 
             profiles are simulated, modelling population heterogeneity in trial arms. 
             Exposures to infectious agents are generated, with infection depending on vitamin D status.  
	"""
	
	cran = "SimVitD" 

	version("1.0.3", md5="8018dbf8b047e92f4d3cd911d4ad3b21")

	depends_on("r-simpleboot", type=("build", "run"))
