# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3shiny(RPackage):
	"""Machine Learning in 'shiny' with 'mlr3'

	A web-based graphical user interface to provide the basic steps of a machine learning workflow. It uses the functionalities of the 'mlr3' framework.
	"""
	
	cran = "mlr3shiny" 

	version("0.3.0", md5="c02ed0984c52bd97aa12a234c2731729")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mlr3@0.12:", type=("build", "run"))
	depends_on("r-mlr3measures@0.3.1:", type=("build", "run"))
	depends_on("r-mlr3learners", type=("build", "run"))
	depends_on("r-mlr3pipelines", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs@2:", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-dt@0.11:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
