# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiverse(RPackage):
	"""'Explorable Multiverse' Data Analysis and Reports

	Implement 'multiverse' style analyses (Steegen S., Tuerlinckx F, Gelman A., Vanpaemal, W., 2016)
    <doi:10.1177/1745691616658637>, (Dragicevic P., Jansen Y., Sarma A., Kay M., Chevalier F., 2019) <doi:10.1145/3290605.3300295> 
    to show the robustness of statistical inference. 'Multiverse analysis' is a philosophy of 
    statistical reporting where paper authors report the outcomes of many different statistical 
    analyses in order to show how fragile or robust their findings are. 
    The 'multiverse' package (Sarma A., Kale A., Moon M., Taback N., Chevalier F., Hullman J., Kay M., 2021) <doi:10.31219/osf.io/yfbwm>
    allows users to concisely and flexibly implement 'multiverse-style' 
    analysis, which involve declaring alternate ways of performing an analysis step, in R and R Notebooks.
	"""
	
	homepage = "https://mucollective.github.io/multiverse/"
	cran = "multiverse" 

	version("0.6.1", md5="c5c796327cc671cc6c16060b0ae2e1b7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr@1.3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-collections", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-berryfunctions", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
