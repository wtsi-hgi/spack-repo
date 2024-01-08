# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RGgdist(RPackage):
	"""Visualizations of Distributions and Uncertainty

	Provides primitives for visualizing distributions using 'ggplot2' that are particularly tuned for
    visualizing uncertainty in either a frequentist or Bayesian mode. Both analytical distributions (such as 
    frequentist confidence distributions or Bayesian priors) and distributions represented as samples (such as 
    bootstrap distributions or Bayesian posterior samples) are easily visualized. Visualization primitives include
    but are not limited to: points with multiple uncertainty intervals, 
    eye plots (Spiegelhalter D., 1999) <https://ideas.repec.org/a/bla/jorssa/v162y1999i1p45-58.html>,
    density plots, gradient plots, dot plots (Wilkinson L., 1999) <doi:10.1080/00031305.1999.10474474>,
    quantile dot plots (Kay M., Kola T., Hullman J., Munson S., 2016) <doi:10.1145/2858036.2858558>,
    complementary cumulative distribution function 
    barplots (Fernandes M., Walls L., Munson S., Hullman J., Kay M., 2018) <doi:10.1145/3173574.3173718>,
    and fit curves with multiple uncertainty ribbons.
	"""
	
	homepage = "https://mjskay.github.io/ggdist/"
	cran = "ggdist" 

	version("3.3.0", md5="c3931d71b1c90056d640f49a24f84ddc")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-dplyr@1.0.0:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.0:", type=("build", "run"))
	depends_on("r-rlang@0.3.0:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-distributional@0.3.2:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
