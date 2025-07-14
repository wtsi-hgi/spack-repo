# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeomics(RPackage):
	"""Time-Course Multi-Omics data integration

	timeOmics is a generic data-driven framework to integrate multi-Omics longitudinal data measured on the same biological samples and select key temporal features with strong associations within the same sample group. The main steps of timeOmics are: 1. Plaform and time-specific normalization and filtering steps; 2. Modelling each biological into one time expression profile; 3. Clustering features with the same expression profile over time; 4. Post-hoc validation step.
	"""
	
	bioc = "timeOmics"

	version("1.20.0", commit="8922b76610b1cf107e5c7980b01cf02ac22e642c")
	version("1.14.0", commit="2965d3c43f02b007053e1d4d8fb458620f3f7da7")

	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
