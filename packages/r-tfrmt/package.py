# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfrmt(RPackage):
	"""Applies Display Metadata to Analysis Results Datasets

	Creates a framework to store and apply display metadata to Analysis
    Results Datasets (ARDs). The use of 'tfrmt' allows users to define table 
    format and styling without the data, and later apply the format to the data.
	"""
	
	homepage = "https://GSK-Biostatistics.github.io/tfrmt/"
	cran = "tfrmt" 

	version("0.1.1", md5="7b1f810504a596fcb13ef1cd3583c911")
	version("0.1.0", md5="91efc763e03e57826c6853d9b3cd1ba6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gt@0.6:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
