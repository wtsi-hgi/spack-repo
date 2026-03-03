# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXhaz(RPackage):
	"""Excess Hazard Modelling Considering Inappropriate Mortality
Rates

	Fits relative survival regression models with or without proportional excess hazards and with the additional possibility to correct for background mortality by one or more parameter(s). These models are relevant when the observed mortality in the studied group is not comparable to that of the general population or in population-based studies where the available life tables used for net survival estimation are insufficiently stratified. In the latter case, the proposed model by Touraine et al. (2020) <doi:10.1177/0962280218823234> can be used. The user can also fit a model that relax the proportional expected hazards assumption considered in the Touraine et al. excess hazard model. This extension was proposed by Mba et al. (2020) <doi:10.1186/s12874-020-01139-z> to allow non-proportional effects of the additional variable on the general population mortality. In non-population-based studies, researchers can identify non-comparability source of bias in terms of expected mortality of selected individuals. A proposed excess hazard model correcting this selection bias is presented in Goungounga et al. (2019) <doi:10.1186/s12874-019-0747-3>. 
	"""
	
	cran = "xhaz" 

	version("2.0.1", md5="631945184fdfab7800bc464b9703a6c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survexp-fr", type=("build", "run"))
