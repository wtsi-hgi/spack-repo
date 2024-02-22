# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpmx(RPackage):
	"""'ggplot2' Based Tool to Facilitate Diagnostic Plots for NLME
Models

	At Novartis, we aimed at standardizing the set of diagnostic plots used for modeling
  activities in order to reduce the overall effort required for generating such plots.
  For this, we developed a guidance that proposes an adequate set of diagnostics and a toolbox,
  called 'ggPMX' to execute them. 'ggPMX' is a toolbox that can generate all diagnostic plots at a quality sufficient
  for publication and submissions using few lines of code. This package focuses on plots recommended by ISoP
  <doi:10.1002/psp4.12161>. While not required, you can get/install the 'R' 'lixoftConnectors'
    package in the 'Monolix' installation, as described at the following url
    <https://monolix.lixoft.com/monolix-api/lixoftconnectors_installation/>.
    When 'lixoftConnectors' is available, 'R' can use 'Monolix' directly to create the required
    Chart Data instead of exporting it from the 'Monolix' gui.
	"""
	
	homepage = "https://github.com/ggPMXdevelopment/ggPMX"
	cran = "ggPMX" 

	version("1.2.11", md5="25b4316af4e13d774838b6019c51007d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
