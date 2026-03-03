# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestmangr(RPackage):
	"""Forest Mensuration and Management

	Processing forest inventory data with methods such as simple random sampling, stratified random sampling and systematic sampling. There are also functions for yield and growth predictions and model fitting, linear and nonlinear grouped data fitting, and statistical tests. References: Kershaw Jr., Ducey, Beers and Husch (2016). <doi:10.1002/9781118902028>.
	"""
	
	homepage = "https://github.com/sollano/forestmangr#readme"
	cran = "forestmangr" 

	version("0.9.6", md5="f14bbfa509d23ed26b6f11eee7905d0a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-systemfit", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-fincal", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
