# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvminer(RPackage):
	"""Drawing Survival Curves using 'ggplot2'

	Contains the function 'ggsurvplot()' for drawing easily beautiful
    and 'ready-to-publish' survival curves with the 'number at risk' table
    and 'censoring count plot'. Other functions are also available to plot 
    adjusted curves for `Cox` model and to visually examine 'Cox' model assumptions.
	"""
	
	homepage = "https://rpkgs.datanovia.com/survminer/index.html"
	cran = "survminer" 

	version("0.4.9", md5="813b1a09bb653a672a1c7cfba544f44c")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr@0.1.6:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-maxstat", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-survmisc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggtext@0.1:", type=("build", "run"))
