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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/timeOmics_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/timeOmics/timeOmics_1.14.0.tar.gz"]

	version("1.14.0", md5="ddea6709cf6d8d977b998f458e7938fb")

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
