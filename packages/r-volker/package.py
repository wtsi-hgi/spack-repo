# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVolker(RPackage):
	"""High-Level Functions for Tabulating, Charting and Reporting
Survey Data

	Craft polished tables and plots in Markdown reports. 
             Simply choose whether to treat your data as counts or metrics, 
             and the package will automatically generate well-designed default tables and plots for you.
             Boiled down to the basics, with labeling features and simple interactive reports.
             All functions are 'tidyverse' compatible.
	"""
	
	homepage = "https://github.com/strohne/volker"
	cran = "volker" 

	version("1.0.2", md5="c05bc4a860b7da0e91f5472d0262e7a4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-skimr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
