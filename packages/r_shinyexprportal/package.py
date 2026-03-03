# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyexprportal(RPackage):
	"""A Configurable 'shiny' Portal for Sharing Analysis of Molecular
Expression Data

	Enables deploying configuration file-based 'shiny' apps with minimal programming for interactive exploration and analysis showcase of molecular expression data. For exploration, supports visualization of correlations between rows of an expression matrix and a table of observations, such as clinical measures, and comparison of changes in expression over time. For showcase, enables visualizing the results of differential expression from package such as 'limma', co-expression modules from 'WGCNA' and lower dimensional projections.
	"""
	
	homepage = "https://c4tb.github.io/shinyExprPortal/"
	cran = "shinyExprPortal" 

	version("1.1.0", md5="d0a8ef982b159e38edc6ee56aef60243")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-iheatmapr", type=("build", "run"))
	depends_on("r-vegawidget", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shinyhelper", type=("build", "run"))
