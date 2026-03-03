# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaconfoundr(RPackage):
	"""Visualize 'Confounder' Control in Meta-Analyses

	Visualize 'confounder' control in meta-analysis.
    'metaconfoundr' is an approach to evaluating bias in studies used in
    meta-analyses based on the causal inference framework. Study groups
    create a causal diagram displaying their assumptions about the
    scientific question. From this, they develop a list of important
    'confounders'. Then, they evaluate whether studies controlled for
    these variables well. 'metaconfoundr' is a toolkit to facilitate this
    process and visualize the results as heat maps, traffic light plots,
    and more.
	"""
	
	homepage = "https://github.com/malcolmbarrett/metaconfoundr"
	cran = "metaconfoundr" 

	version("0.1.2", md5="d68356ab3b69d5d8b95fc5dd87556b84")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
