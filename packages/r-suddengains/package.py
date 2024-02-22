# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuddengains(RPackage):
	"""Identify Sudden Gains in Longitudinal Data

	Identify sudden gains based on the three criteria outlined by Tang and DeRubeis (1999) <doi:10.1037/0022-006X.67.6.894> to a selection of repeated measures. Sudden losses, defined as the opposite of sudden gains can also be identified. Two different datasets can be created, one including all sudden gains/losses and one including one selected sudden gain/loss for each case. It can extract scores around sudden gains/losses. It can plot the average change around sudden gains/losses and trajectories of individual cases.
	"""
	
	homepage = "https://milanwiedemann.github.io/suddengains/"
	cran = "suddengains" 

	version("0.7.2", md5="0756e9c0b3bcb492d9779bd461b0a11f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-psych@1.8.12:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.2:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-patchwork@1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-naniar", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
