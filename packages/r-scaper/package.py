# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScaper(RPackage):
	"""Single Cell Transcriptomics-Level Cytokine Activity Prediction
and Estimation

	Generates cell-level cytokine activity estimates using relevant information from gene sets constructed with the 'CytoSig' and the 'Reactome' databases and scored using the modified 'Variance-adjusted Mahalanobis (VAM)' framework for single-cell RNA-sequencing (scRNA-seq) data. 'CytoSig' database is described in: Jiang at al., (2021) <doi:10.1038/s41592-021-01274-5>. 'Reactome' database is described in: Gillespie et al., (2021) <doi:10.1093/nar/gkab1028>. The 'VAM' method is outlined in: Frost (2020) <doi:10.1093/nar/gkaa582>.
	"""
	
	cran = "scaper" 

	version("0.1.0", md5="362249ded55d0be44333496038d3d7c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
	depends_on("r-vam", type=("build", "run"))
