# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVannstats(RPackage):
	"""Simplified Statistics for PA 606

	Simplifies functions assess normality for bivariate and multivariate statistical techniques. Includes functions designed to replicate plots and tables that would result from similar calls in 'SPSS', including hst(), box(), qq(), tab(), cormat(), and residplot(). Also includes simplified formulae, such as mode(), scatter(), p.corr(), ow.anova(), and rm.anova().
	"""
	
	cran = "vannstats" 

	version("1.3.4.14", md5="ed2e2b76e29a5f07306a5cd1f98e65ae")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
