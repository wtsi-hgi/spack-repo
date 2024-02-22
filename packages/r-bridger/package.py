# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBridger(RPackage):
	"""Bridge Hand Generator with Criteria Selector

	Produce bridge hands, allowing parameters for hands to offer specific for bidding sequences.
	"""
	
	homepage = "https://github.com/CommoditiesAI/bridger"
	cran = "bridger" 

	version("0.1.0", md5="e33f96f5ea2bd623da886d770359bf44")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggedit", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
