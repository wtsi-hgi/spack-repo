# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArmada(RPackage):
	"""A Statistical Methodology to Select Covariates in
High-Dimensional Data under Dependence

	Two steps variable selection procedure in a context of high-dimensional dependent data
  but few observations. First step is dedicated to eliminate dependence between variables (clustering
  of variables, followed by factor analysis inside each cluster).
  Second step is a variable selection using by aggregation of adapted methods.
  Bastien B., Chakir H., Gegout-Petit A., Muller-Gueudin A., Shi Y.
  A statistical methodology to select covariates in high-dimensional data under dependence.
  Application to the classification of genetic profiles associated with outcome of a non-small-cell
  lung cancer treatment. 2018. <https://hal.archives-ouvertes.fr/hal-01939694>.
	"""
	
	cran = "armada" 

	version("0.1.0", md5="1035536b113ba8fe94acab4b72f8487d")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-clustofvar", type=("build", "run"))
	depends_on("r-famt", type=("build", "run"))
	depends_on("r-vsurf", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-anapuce", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
