# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REhdprep(RPackage):
	"""Quality Control and Semantic Enrichment of Datasets

	A tool for the preparation and enrichment of health datasets for analysis (Toner et al. (2023) <doi:10.1093/gigascience/giad030>). Provides functionality for assessing data quality and for improving the reliability and machine interpretability of a dataset. 
     'eHDPrep' also enables semantic enrichment of a dataset where metavariables are discovered from the relationships between input variables determined from user-provided ontologies.
	"""
	
	homepage = "https://github.com/overton-group/eHDPrep"
	cran = "eHDPrep" 

	version("1.3.3", md5="86633ab007d74a063996e9c8480de386")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-kableextra@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.5:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-quanteda@2.1.2:", type=("build", "run"))
	depends_on("r-tm@0.7.8:", type=("build", "run"))
	depends_on("r-pheatmap@1.0.12:", type=("build", "run"))
	depends_on("r-igraph@1.2.6:", type=("build", "run"))
	depends_on("r-tidygraph@1.2:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-knitr@1.31:", type=("build", "run"))
