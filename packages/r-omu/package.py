# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmu(RPackage):
	"""A Metabolomics Analysis Tool for Intuitive Figures and
Convenient Metadata Collection

	Facilitates the creation of intuitive figures to describe metabolomics data by utilizing Kyoto Encyclopedia of Genes and Genomes (KEGG) hierarchy data, and gathers functional orthology and gene data from the KEGG-REST API.
	"""
	
	homepage = "https://github.com/connor-reid-tiffany/Omu"
	cran = "omu" 

	version("1.1.2", md5="3a3cea76dad8985f7c22cb68ee975cea")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-fsa", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
