# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMocha(RPackage):
	"""Modeling for Single-Cell Open Chromatin Analysis

	A statistical framework and analysis tool for open chromatin 
  analysis designed specifically for single cell ATAC-seq (Assay for 
  Transposase-Accessible Chromatin) data, after cell type/cluster 
  identification. These novel modules remove unwanted technical variation, 
  identify open chromatin, robustly models repeated measures in single cell 
  data, implement advanced statistical frameworks to model zero-inflation for 
  differential and co-accessibility analyses, and integrate with existing 
  databases and modules for downstream analyses to reveal biological insights. 
  MOCHA provides a statistical foundation for complex downstream analysis to 
  help advance the potential of single cell ATAC-seq for applied studies. 
  Methods for zero-inflated statistics are as described in: 
  Ghazanfar, S., Lin, Y., Su, X. et al. (2020) <doi:10.1038/s41592-020-0885-x>.
  Pimentel, Ronald Silva, "Kendall's Tau and Spearman's Rho for Zero-Inflated 
  Data" (2009) <https://scholarworks.wmich.edu/dissertations/721/>.
	"""
	
	cran = "MOCHA" 

	version("1.1.0", md5="033a8caff09292ba390f12dd72c3ec4e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyranges@1.14:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-wcorr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
