# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForesight(RPackage):
	"""Systems Insights from Generation of Hydroclimatic Timeseries

	A tool to create hydroclimate scenarios, stress test systems and visualize system performance in scenario-neutral climate change impact assessments. Scenario-neutral approaches 'stress-test' the performance of a modelled system by applying a wide range of plausible hydroclimate conditions (see Brown & Wilby (2012) <doi:10.1029/2012EO410001> and Prudhomme et al. (2010) <doi:10.1016/j.jhydrol.2010.06.043>). These approaches allow the identification of hydroclimatic variables that affect the vulnerability of a system to hydroclimate variation and change. This tool enables the generation of perturbed time series using a range of approaches including simple scaling of observed time series (e.g. Culley et al. (2016) <doi:10.1002/2015WR018253>) and stochastic simulation of perturbed time series via an inverse approach (see Guo et al. (2018) <doi:10.1016/j.jhydrol.2016.03.025>). It incorporates 'Richardson-type' weather generator model configurations documented in Richardson (1981) <doi:10.1029/WR017i001p00182>, Richardson and Wright (1984), as well as latent variable type model configurations documented in Bennett et al. (2018) <doi:10.1016/j.jhydrol.2016.12.043>, Rasmussen (2013) <doi:10.1002/wrcr.20164>, Bennett et al. (2019) <doi:10.5194/hess-23-4783-2019> to generate hydroclimate variables on a daily basis (e.g. precipitation, temperature, potential evapotranspiration) and allows a variety of different hydroclimate variable properties, herein called attributes, to be perturbed. Options are included for the easy integration of existing system models both internally in R and externally for seamless 'stress-testing'. A suite of visualization options for the results of a scenario-neutral analysis (e.g. plotting performance spaces and overlaying climate projection information) are also included. Version 1.0 of this package is described in Bennett et al. (2021) <doi:10.1016/j.envsoft.2021.104999>. As further developments in scenario-neutral approaches occur the tool will be updated to incorporate these advances.
	"""
	
	cran = "foreSIGHT" 

	version("1.2.0", md5="be3d5ea1bb242022f54974e9b4063496")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ga@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-directlabels", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcorpora", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-soilhyp", type=("build", "run"))
	depends_on("r-cmaes", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-rgn", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
