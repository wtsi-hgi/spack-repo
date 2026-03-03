# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REwsmethods(RPackage):
	"""Forecasting Tipping Points at the Community Level

	Rolling and expanding window approaches to assessing abundance based early warning signals, non-equilibrium resilience measures, and machine learning. See Dakos et al. (2012) <doi:10.1371/journal.pone.0041010>, Deb et al. (2022) <doi:10.1098/rsos.211475>, Drake and Griffen (2010) <doi:10.1038/nature09389>, Ushio et al. (2018) <doi:10.1038/nature25504> and Weinans et al. (2021) <doi:10.1038/s41598-021-87839-y> for methodological details. Graphical presentation of the outputs are also provided for clear and publishable figures. Visit the 'EWSmethods' website for more information, and tutorials.
	"""
	
	homepage = "https://github.com/duncanobrien/EWSmethods"
	cran = "EWSmethods" 

	version("1.2.5", md5="275b1adeb5ebd06b7514a2ff3163ff0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-mar", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-redm@1.15:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
