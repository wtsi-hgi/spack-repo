# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHidecan(RPackage):
	"""Create HIDECAN Plots for Visualising Genome-Wide Association
Studies and Differential Expression Results

	Generates HIDECAN plots that summarise and combine 
  the results of genome-wide association studies (GWAS) and transcriptomics 
  differential expression analyses (DE), along with manually curated candidate genes of interest. The HIDECAN plot 
  is presented in Angelin-Bonnet et al. (2023) (currently in review).
	"""
	
	homepage = "https://plantandfoodresearch.github.io/hidecan/"
	cran = "hidecan" 

	version("1.1.0", md5="d5e47f16faac70d6ad478811b4d65b59")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
