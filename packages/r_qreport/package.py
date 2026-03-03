# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQreport(RPackage):
	"""Statistical Reporting with 'Quarto'

	Provides statistical components, tables, and graphs
    that are useful in 'Quarto' and 'RMarkdown' reports and that produce 'Quarto'
    elements for special formatting such as tabs and marginal notes and graphs.
    Some of the functions produce entire report sections with tabs, e.g.,
    the missing data report created by missChk().  Functions for inserting
		variables and tables inside 'graphviz' and 'mermaid' diagrams are included,
		and so are special clinical trial graphics for adverse event reporting.
	"""
	
	homepage = "https://hbiostat.org/R/qreport/"
	cran = "qreport" 

	version("1.0-0", md5="29fc6775683069ff618f79f195058c30")

	depends_on("r-hmisc@5.1.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
