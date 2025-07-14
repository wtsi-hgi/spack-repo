# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSystempiper(RPackage):
	"""systemPipeR: workflow management and report generation environment

	systemPipeR is a multipurpose data analysis workflow environment that unifies R with command-line tools. It enables scientists to analyze many types of large- or small-scale data on local or distributed computer systems with a high level of reproducibility, scalability and portability. At its core is a command-line interface (CLI) that adopts the Common Workflow Language (CWL). This design allows users to choose for each analysis step the optimal R or command-line software. It supports both end-to-end and partial execution of workflows with built-in restart functionalities. Efficient management of complex analysis tasks is accomplished by a flexible workflow control container class. Handling of large numbers of input samples and experimental designs is facilitated by consistent sample annotation mechanisms. As a multi-purpose workflow toolkit, systemPipeR enables users to run existing workflows, customize them or design entirely new ones while taking advantage of widely adopted data structures within the Bioconductor ecosystem. Another important core functionality is the generation of reproducible scientific analysis and technical reports. For result interpretation, systemPipeR offers a wide range of plotting functionality, while an associated Shiny App offers many useful functionalities for interactive result exploration. The vignettes linked from this page include (1) a general introduction, (2) a description of technical details, and (3) a collection of workflow templates.
	"""
	
	homepage = "https://systempipe.org/"
	bioc = "systemPipeR"

	version("2.14.2", commit="8f2eb62b695f5d35e041410ecfa6c67458f69e9a")
	version("2.8.0", commit="7cfd2370ff93a6034fa626356df04b8079929671")

	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-shortread@1.37.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
