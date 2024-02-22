# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlorr(RPackage):
	"""Tools for Developing Binary Logistic Regression Models

	Tools designed to make it easier for beginner and intermediate users to build and validate 
    binary logistic regression models. Includes bivariate analysis, comprehensive regression output, 
    model fit statistics, variable selection procedures, model validation techniques and a 'shiny' 
    app for interactive model building.
	"""
	
	homepage = "URL:"
	cran = "blorr" 

	version("0.3.0", md5="34fd00754254a1734cda8307e1a417bf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lest", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
