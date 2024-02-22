# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemgraph(RPackage):
	"""Network Analysis and Causal Inference Through Structural
Equation Modeling

	Estimate networks and causal relationships in complex systems through
  Structural Equation Modeling. This package also includes functions to import,
  weight, manipulate, and fit biological network models within the
  Structural Equation Modeling framework proposed in
  Grassi M, Palluzzi F, Tarantino B (2022) <doi:10.1093/bioinformatics/btac567>.
	"""
	
	homepage = "https://github.com/fernandoPalluzzi/SEMgraph"
	cran = "SEMgraph" 

	version("1.2.1", md5="dddf529780a07f6d9dba307b19b4db9d")

	depends_on("r-igraph@1.6:", type=("build", "run"))
	depends_on("r-lavaan@0.6.1:", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-aspect", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-dagitty", type=("build", "run"))
	depends_on("r-flip", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-ggm", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-protoclust", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
