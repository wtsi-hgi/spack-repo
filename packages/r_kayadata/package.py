# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKayadata(RPackage):
	"""Kaya Identity Data for Nations and Regions

	Provides data for Kaya identity variables (population, gross 
             domestic product, primary energy consumption, and energy-related 
             CO2 emissions) for the world and for individual nations, and 
             utility functions for looking up data,  plotting trends of 
             Kaya variables, and plotting the fuel mix for a given country
             or region. The Kaya identity (Yoichi Kaya and Keiichi Yokobori, 
             "Environment, Energy, and Economy: Strategies for Sustainability" 
             (United Nations University Press, 1998) and 
             <https://en.wikipedia.org/wiki/Kaya_identity>) expresses a nation's 
             or region's greenhouse gas emissions in terms of its population, 
             per-capita Gross Domestic Product, the energy intensity of its 
             economy, and the carbon-intensity of its energy supply.
	"""
	
	homepage = "https://jonathan-g.github.io/kayadata/"
	cran = "kayadata" 

	version("1.3.0", md5="95a2bd12d7f9239bce83e49a5e8a5972")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-forcats@0.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
