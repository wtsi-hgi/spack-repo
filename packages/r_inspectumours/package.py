# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInspectumours(RPackage):
	"""IN-vivo reSPonsE Classification of Tumours

	This is a shiny app used for the statistical classifying and analysing
    pre-clinical tumour responses.
	"""
	
	cran = "INSPECTumours" 

	version("0.1.0", md5="72fc107cfa68a961176f6d1f08b01c56")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggeffects", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-modelr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinytoastr", type=("build", "run"))
	depends_on("r-shinyvalidate", type=("build", "run"))
	depends_on("r-tidybayes", type=("build", "run"))
	depends_on("r-tippy", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
