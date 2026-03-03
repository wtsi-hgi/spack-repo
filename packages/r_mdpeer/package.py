# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdpeer(RPackage):
	"""Graph-Constrained Regression with Enhanced Regularization
Parameters Selection

	Provides graph-constrained regression methods in which
    regularization parameters are selected automatically via estimation of
    equivalent Linear Mixed Model formulation. 'riPEER' (ridgified Partially
    Empirical Eigenvectors for Regression) method employs a penalty term being
    a linear combination of graph-originated and ridge-originated penalty terms,
    whose two regularization parameters are ML estimators from corresponding
    Linear Mixed Model solution; a graph-originated penalty term allows imposing
    similarity between coefficients based on graph information given whereas
    additional ridge-originated penalty term facilitates parameters estimation:
    it reduces computational issues arising from singularity in a graph-originated
    penalty matrix and yields plausible results in situations when graph information
    is not informative. 'riPEERc' (ridgified Partially Empirical Eigenvectors
    for Regression with constant) method utilizes addition of a diagonal matrix
    multiplied by a predefined (small) scalar to handle the non-invertibility of
    a graph Laplacian matrix. 'vrPEER' (variable reducted PEER) method performs
    variable-reduction procedure to handle the non-invertibility of a graph
    Laplacian matrix.
	"""
	
	cran = "mdpeer" 

	version("1.0.1", md5="cbf3c9a00441019b3dac35e430c78b3c")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
