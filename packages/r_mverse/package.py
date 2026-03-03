# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMverse(RPackage):
	"""Tidy Multiverse Analysis Made Simple

	Extends 'multiverse' package
    (Sarma A., Kale A., Moon M., Taback N., Chevalier F., Hullman J., Kay M., 2021)
    <doi:10.31219/osf.io/yfbwm>, which allows users perform to create explorable
    multiverse analysis in R. This extension provides an additional level of
    abstraction to the 'multiverse' package with the aim of creating
    user friendly syntax to researchers, educators, and students in statistics.
    The 'mverse' syntax is designed to allow piping and takes hints from
    the 'tidyverse' grammar. The package allows users to define and inspect
    multiverse analysis using familiar syntax in R.
	"""
	
	homepage = "https://github.com/mverseanalysis/mverse/"
	cran = "mverse" 

	version("0.1.0", md5="f17860e73d32214addce01d5f1f7aade")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-multiverse", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
