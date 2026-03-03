# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmse(RPackage):
	"""Generalised Management Strategy Evaluation Simulator

	Integrates game theory and ecological theory to construct 
    social-ecological models that simulate the management of populations and 
    stakeholder actions. These models build off of a previously developed 
    management strategy evaluation (MSE) framework to simulate all aspects of 
    management: population dynamics, manager observation of populations, manager
    decision making, and stakeholder responses to management decisions. The 
    newly developed generalised management strategy evaluation (GMSE) 
    framework uses genetic algorithms to mimic the decision-making process of 
    managers and stakeholders under conditions of change, uncertainty, and 
    conflict. Simulations can be run using gmse(), gmse_apply(), and
    gmse_gui() functions.
	"""
	
	homepage = "https://confoobio.github.io/gmse/"
	cran = "GMSE" 

	version("1.0.0.2", md5="73602dfc0a02aa9c9c7b062c06ccca7f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
