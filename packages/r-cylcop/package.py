# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCylcop(RPackage):
	"""Circular-Linear Copulas with Angular Symmetry for Movement Data

	Classes (S4) of circular-linear, symmetric copulas with corresponding
    methods, extending the 'copula' package. These copulas are especially useful
    for modeling correlation in discrete-time movement data. Methods for density, 
    (conditional) distribution, random number generation, bivariate dependence
    measures and fitting parameters using maximum likelihood and other 
    approaches. The package also contains methods for visualizing movement data
    and copulas.
	"""
	
	homepage = "https://github.com/r-lib/devtools"
	cran = "cylcop" 

	version("0.2.0", md5="272f53fc3de906bc866f28ebe2854455")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-gofkernel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mixr", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
