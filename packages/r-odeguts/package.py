# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdeguts(RPackage):
	"""Solve ODE for GUTS-RED-SD and GUTS-RED-IT Using Compiled Code

	Allows performing forwards prediction for the General Unified 
          Threshold model of Survival using compiled ode code. This package 
          was created to avoid dependency with the 'morse' package that requires 
          the installation of 'JAGS'. This package is based on functions from 
          the 'morse' package v3.3.1: Virgile Baudrot, Sandrine Charles, 
          Marie Laure Delignette-Muller, Wandrille Duchemin, Benoit Goussen, 
          Nils Kehrein, Guillaume Kon-Kam-King, Christelle Lopes, Philippe Ruiz, 
          Alexander Singer and Philippe Veber (2021) <https://CRAN.R-project.org/package=morse>.
	"""
	
	homepage = "https://github.com/bgoussen/odeGUTS"
	cran = "odeGUTS" 

	version("1.0.2", md5="61d7df94e0fb6ee57212154313abedb8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
