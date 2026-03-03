# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasket(RPackage):
	"""Basket Trial Analysis

	Implementation of multisource exchangeability models for Bayesian analyses of prespecified subgroups arising in the context of basket trial design and monitoring.  The R 'basket' package facilitates implementation of the binary, symmetric multi-source exchangeability model (MEM) with posterior inference arising from both exact computation and Markov chain Monte Carlo sampling. Analysis output includes full posterior samples as well as posterior probabilities, highest posterior density (HPD) interval boundaries, effective sample sizes (ESS), mean and median estimations, posterior exchangeability probability matrices, and maximum a posteriori MEMs. In addition to providing "basketwise" analyses, the package includes similar calculations for "clusterwise" analyses for which subgroups are combined into meta-baskets, or clusters, using graphical clustering algorithms that treat the posterior exchangeability probabilities as edge weights. In addition plotting tools are provided to visualize basket and cluster densities as well as their exchangeability.  References include Hyman, D.M., Puzanov, I., Subbiah, V., Faris, J.E., Chau, I., Blay, J.Y., Wolf, J., Raje, N.S., Diamond, E.L., Hollebecque, A. and Gervais, R (2015) <doi:10.1056/NEJMoa1502309>; Hobbs, B.P. and Landin, R. (2018) <doi:10.1002/sim.7893>; Hobbs, B.P., Kane, M.J., Hong, D.S. and Landin, R. (2018) <doi:10.1093/annonc/mdy457>; and Kaizer, A.M., Koopmeiners, J.S. and Hobbs, B.P. (2017) <doi:10.1093/biostatistics/kxx031>.
	"""
	
	homepage = "https://github.com/kaneplusplus/basket"
	cran = "basket" 

	version("0.10.11", md5="b5daccaf3c55189a09b697861e682aee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
