# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelsummary(RPackage):
	"""Create Publication-Ready Regression Tables with Panels

	Create an automated regression table that is well-suited for models that are estimated with multiple dependent variables. 'panelsummary' extends 'modelsummary' (Arel-Bundock, V. (2022) <doi:10.18637/jss.v103.i01>) by allowing regression tables to be split into multiple sections with a simple function call. Utilize familiar arguments such as fmt, estimate, statistic, vcov, conf_level, stars, coef_map, coef_omit, coef_rename, gof_map, and gof_omit from 'modelsummary' to clean the table, and additionally, add a row for the mean of the dependent variable without external manipulation. 
	"""
	
	homepage = "https://github.com/michaeltopper1/panelsummary"
	cran = "panelsummary" 

	version("0.1.2.1", md5="79ce287a6e2e6b3a62eca0a0114b3e38")

	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-fixest@0.10.4:", type=("build", "run"))
	depends_on("r-kableextra@1.3.4:", type=("build", "run"))
	depends_on("r-modelsummary@1.3:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
