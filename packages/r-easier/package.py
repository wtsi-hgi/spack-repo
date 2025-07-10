# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasier(RPackage):
	"""Estimate Systems Immune Response from RNA-seq data

	This package provides a workflow for the use of EaSIeR tool, developed to assess patients' likelihood to respond to ICB therapies providing just the patients' RNA-seq data as input. We integrate RNA-seq data with different types of prior knowledge to extract quantitative descriptors of the tumor microenvironment from several points of view, including composition of the immune repertoire, and activity of intra- and extra-cellular communications. Then, we use multi-task machine learning trained in TCGA data to identify how these descriptors can simultaneously predict several state-of-the-art hallmarks of anti-cancer immune response. In this way we derive cancer-specific models and identify cancer-specific systems biomarkers of immune response. These biomarkers have been experimentally validated in the literature and the performance of EaSIeR predictions has been validated using independent datasets form four different cancer types with patients treated with anti-PD1 or anti-PDL1 therapy.
	"""
	
	bioc = "easier" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/easier_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/easier/easier_1.8.0.tar.gz"]

	version("1.8.0", sha256="61cf117669aefd4b1369fde5444717f870b96320701339b86a2336b5617a8f52")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-progeny", type=("build", "run"))
	depends_on("r-easierdata", type=("build", "run"))
	depends_on("r-dorothea@1.6:", type=("build", "run"))
	depends_on("r-decoupler", type=("build", "run"))
	depends_on("r-quantiseqr", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
