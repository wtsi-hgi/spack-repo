# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmunarch(RPackage):
	"""Bioinformatics Analysis of T-Cell and B-Cell Immune Repertoires

	A comprehensive framework for bioinformatics exploratory analysis of bulk and single-cell
    T-cell receptor and antibody repertoires. It provides seamless data loading, analysis and
    visualisation for AIRR (Adaptive Immune Receptor Repertoire) data, both bulk immunosequencing (RepSeq)
    and single-cell sequencing (scRNAseq). Immunarch implements most of the widely used AIRR analysis methods,
    such as: clonality analysis, estimation of repertoire similarities in distribution of clonotypes
    and gene segments, repertoire diversity analysis, annotation of clonotypes using external immune receptor
    databases and clonotype tracking in vaccination and cancer studies. A successor to our
    previously published 'tcR' immunoinformatics package (Nazarov 2015) <doi:10.1186/s12859-015-0613-1>.
	"""
	
	homepage = "https://immunarch.com/"
	cran = "immunarch" 

	version("0.9.1", md5="a1f53c8576244a0c6d23df01fef12b76")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-dtplyr@1:", type=("build", "run"))
	depends_on("r-data-table@1.12.6:", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-factoextra@1.0.4:", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-upsetr@1.4:", type=("build", "run"))
	depends_on("r-pheatmap@1.0.12:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-rtsne@0.15:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-airr", type=("build", "run"))
	depends_on("r-ggseqlogo", type=("build", "run"))
	depends_on("r-ggalluvial@0.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggpubr@0.2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
