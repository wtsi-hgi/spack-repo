# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpandar(RPackage):
	"""Explore Your Data Interactively

	Provides a shiny-based front end (the 'ExPanD' app) and
    a set of functions for exploratory data analysis. Run as a web-based 
    app, 'ExPanD' enables users to assess the robustness of empirical evidence 
    without providing them access to the underlying data. You can export a 
    notebook containing the analysis of 'ExPanD' and/or use the functions of the 
    package to support your exploratory data analysis workflow. Refer to the 
    vignettes of the package for more information on how to use 'ExPanD' and/or 
    the functions of this package.
	"""
	
	homepage = "https://joachim-gassen.github.io/ExPanDaR/"
	cran = "ExPanDaR" 

	version("0.5.3", md5="035033d9ed4befe57b8c2791d6ed80d6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-multiwayvcov", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-stargazer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
