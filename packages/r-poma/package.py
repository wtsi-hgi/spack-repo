# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoma(RPackage):
	"""Tools for Omics Data Analysis

	A reproducible and easy-to-use toolkit for visualization, pre-processing, exploration, and statistical analysis of omics datasets. The main aim of POMA is to enable a flexible data cleaning and statistical analysis processes in one comprehensible and user-friendly R package. This package has a Shiny app version called POMAShiny that implements all POMA functions. See https://github.com/pcastellanoescuder/POMAShiny. See Castellano-Escuder P, González-Domínguez R, Carmona-Pontaque F, et al. (2021) <doi:10.1371/journal.pcbi.1009148> for more details.
	"""
	
	homepage = "https://github.com/pcastellanoescuder/POMA"
	bioc = "POMA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/POMA_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/POMA/POMA_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="83f550759c222e7aa4a640a6bdb0ce8e66445d5389d96f7487d8ac624b7db921")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-glasso@1.11:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rankprod@3.14:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
