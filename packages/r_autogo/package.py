# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutogo(RPackage):
	"""Auto-GO: Reproducible, Robust and High Quality Ontology
Enrichment Visualizations

	Auto-GO is a framework that enables automated, high quality Gene Ontology enrichment analysis visualizations. It also features a handy wrapper for Differential Expression analysis around the 'DESeq2' package described in Love et al. (2014) <doi:10.1186/s13059-014-0550-8>. The whole framework is structured in different, independent functions, in order to let the user decide which steps of the analysis to perform and which plot to produce.
	"""
	
	cran = "autoGO" 

	version("0.9.1", md5="c211045c8fb6a3ec8b1d744158a0ff0c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-enrichr", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dichromat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-imgur", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-textshape", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
