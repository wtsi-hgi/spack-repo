# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamat(RPackage):
	"""Functional analysis of metabolic and transcriptomic data

	Famat is made to collect data about lists of genes and metabolites provided by user, and to visualize it through a Shiny app. Information collected is: - Pathways containing some of the user's genes and metabolites (obtained using a pathway enrichment analysis). - Direct interactions between user's elements inside pathways. - Information about elements (their identifiers and descriptions). - Go terms enrichment analysis performed on user's genes. The Shiny app is composed of: - information about genes, metabolites, and direct interactions between them inside pathways. - an heatmap showing which elements from the list are in pathways (pathways are structured in hierarchies). - hierarchies of enriched go terms using Molecular Function and Biological Process.
	"""
	
	homepage = "https://github.com/emiliesecherre/famat"
	bioc = "famat" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/famat_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/famat/famat_1.12.0.tar.gz"]

	version("1.12.0", sha256="d2da9308e980817f3e8a85a7d5f09cc90df857ffb3b059b6687d2f359929f706")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gprofiler2", type=("build", "run"))
	depends_on("r-rwikipathways", type=("build", "run"))
	depends_on("r-reactome-db", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
