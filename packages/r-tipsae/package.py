# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTipsae(RPackage):
	"""Tools for Handling Indices and Proportions in Small Area
Estimation

	It allows for mapping proportions and indicators defined on the unit interval. It implements Beta-based small area methods comprising the classical Beta regression models, the Flexible Beta model and Zero and/or One Inflated extensions (Janicki 2020 <doi:10.1080/03610926.2019.1570266>). Such methods, developed within a Bayesian framework through Stan <https://mc-stan.org/>, come equipped with a set of diagnostics and complementary tools, visualizing and exporting functions. A Shiny application with a user-friendly interface can be launched to further simplify the process. For further details, refer to De Nicolò and Gardini (2024 <doi:10.18637/jss.v108.i01>).
	"""
	
	cran = "tipsae" 

	version("1.0.0", md5="08278bbcc06f80ecdc85988b81f6ecea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.0.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-nlme@3.1.152:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "link", "run"))
