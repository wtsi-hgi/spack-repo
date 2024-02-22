# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycdisc(RPackage):
	"""Quick Table Generation & Exploratory Analyses on ADaM-Ish
Datasets

	Provides users a quick exploratory dive into common
    visualizations without writing a single line of code given the users
    data follows the Analysis Data Model (ADaM) standards put forth by the
    Clinical Data Interchange Standards Consortium (CDISC)
    <https://www.cdisc.org>. Prominent modules/ features of the
    application are the Table Generator, Population Explorer, and the
    Individual Explorer. The Table Generator allows users to drag and drop
    variables and desired statistics (frequencies, means, ANOVA, t-test,
    and other summary statistics) into bins that automagically create
    stunning tables with validated information. The Population Explorer
    offers various plots to visualize general trends in the population
    from various vantage points. Plot modules currently include scatter
    plot, spaghetti plot, box plot, histogram, means plot, and bar plot.
    Each plot type allows the user to plot uploaded variables against one
    another, and dissect the population by filtering out certain subjects.
    Last, the Individual Explorer establishes a cohesive patient
    narrative, allowing the user to interact with patient metrics (params)
    by visit or plotting important patient events on a timeline. All
    modules allow for concise filtering & downloading bulk outputs into
    html or pdf formats to save for later.
	"""
	
	homepage = "https://github.com/Biogen-Inc/tidyCDISC/"
	cran = "tidyCDISC" 

	version("0.2.1", md5="2a20ac459fd1aa1a6ade4762468660ac")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cicerone", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-ideafilter", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-timevis", type=("build", "run"))
	depends_on("r-tippy@0.1", type=("build", "run"))
