# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuge(RPackage):
	"""High-Dimensional Undirected Graph Estimation

	Provides a general framework for
        high-dimensional undirected graph estimation. It integrates
        data preprocessing, neighborhood screening, graph estimation,
        and model selection techniques into a pipeline. In
        preprocessing stage, the nonparanormal(npn) transformation is
        applied to help relax the normality assumption. In the graph
        estimation stage, the graph structure is estimated by
        Meinshausen-Buhlmann graph estimation or the graphical lasso,
        and both methods can be further accelerated by the lossy
        screening rule preselecting the neighborhood of each variable
        by correlation thresholding. We target on high-dimensional data
        analysis usually d >> n, and the computation is
        memory-optimized using the sparse matrix output. We also
        provide a computationally efficient approach, correlation
        thresholding graph estimation. Three
        regularization/thresholding parameter selection methods are
        included in this package: (1)stability approach for
        regularization selection (2) rotation information criterion (3)
        extended Bayesian information criterion which is only available
        for the graphical lasso.
	"""
	
	cran = "huge" 

	version("1.3.5", md5="e3a906b28fc973623614b4a50c5ea42c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
