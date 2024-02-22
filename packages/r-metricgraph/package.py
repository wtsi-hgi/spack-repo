# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetricgraph(RPackage):
	"""Random Fields on Metric Graphs

	Facilitates creation and manipulation of metric graphs, such as street or river networks. Further facilitates operations and visualizations of data on metric graphs, and the creation of a large class of random fields and stochastic partial differential equations on such spaces. These random fields can be used for simulation, prediction and inference. In particular, linear mixed effects models including random field components can be fitted to data based on computationally efficient sparse matrix representations. Interfaces to the R packages 'INLA' and 'inlabru' are also provided, which facilitate working with Bayesian statistical models on metric graphs. The main references for the methods are Bolin, Simas and Wallin (2022) <doi:10.48550/arXiv.2205.06163>, Bolin, Kovacs, Kumar and Simas (2023) <doi:10.48550/arXiv.2302.03995> and Bolin, Simas and Wallin (2023) <doi:10.48550/arXiv.2304.03190> and <doi:10.48550/arXiv.2304.10372>.
	"""
	
	homepage = "https://davidbolin.github.io/MetricGraph/"
	cran = "MetricGraph" 

	version("1.2.0", md5="f1ebc6ab82c152ac1f5acd34d5c4ad9e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rspde@2.3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
