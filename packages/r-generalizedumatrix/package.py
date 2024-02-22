# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneralizedumatrix(RPackage):
	"""Credible Visualization for Two-Dimensional Projections of Data

	Projections are common dimensionality reduction methods, which represent high-dimensional data in a two-dimensional space. However, when restricting the output space to two dimensions, which results in a two dimensional scatter plot (projection) of the data, low dimensional similarities do not represent high dimensional distances coercively [Thrun, 2018] <DOI: 10.1007/978-3-658-20540-9>. This could lead to a misleading interpretation of the underlying structures [Thrun, 2018]. By means of the 3D topographic map the generalized Umatrix is able to depict errors of these two-dimensional scatter plots. The package is derived from the book of Thrun, M.C.: "Projection Based Clustering through Self-Organization and Swarm Intelligence" (2018) <DOI:10.1007/978-3-658-20540-9> and the main algorithm called simplified self-organizing map for dimensionality reduction methods is published in <DOI: 10.1016/j.mex.2020.101093>.
	"""
	
	homepage = "https://www.deepbionics.org"
	cran = "GeneralizedUmatrix" 

	version("1.2.6", md5="e60c6218259d6147f797dd73e8af365a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
