# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmdi(RPackage):
	"""Perform Structural Missing Data Investigations

	An easy to use implementation of routine structural missing data diagnostics with functions to visualize the proportions of missing observations, investigate missing data patterns and conduct various empirical missing data diagnostic tests. Reference: Weberpals J, Raman SR, Shaw PA, Lee H, Russo M, Hammil BG, Toh D, Connolly JG, Dandreo KJ, Tian F, Liu W, Li Jie, Hernandez-Munos JJ, Glynn RJ, Desai RJ (2023, in submission). "A Principled Approach to Characterize and Analyze Partially Observed Confounder Data From Electronic Health Records: A Plasmode Simulation Study."
	"""
	
	homepage = "https://janickweberpals.gitlab-pages.partners.org/smdi"
	cran = "smdi" 

	version("0.2.2", md5="3c8f37488fb2f40c132abb0831d3a0fb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-hotelling", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-naniar", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
