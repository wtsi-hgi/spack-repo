# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcsub(RPackage):
	"""A Bayesian Semiparametric Factor Analysis Model for Subtype
Identification (Clustering)

	Gene expression profiles are commonly utilized to infer disease
             subtypes and many clustering methods can be adopted for this task.
             However, existing clustering methods may not perform well when
             genes are highly correlated and many uninformative genes are included
             for clustering. To deal with these challenges, we develop a novel
             clustering method in the Bayesian setting. This method, called BCSub,
             adopts an innovative semiparametric Bayesian factor analysis model
             to reduce the dimension of the data to a few factor scores for
             clustering. Specifically, the factor scores are assumed to follow
             the Dirichlet process mixture model in order to induce clustering.
	"""
	
	cran = "BCSub" 

	version("0.5", md5="97b764222360e2ebcff40e5699587ed2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-mcclust@1:", type=("build", "run"))
	depends_on("r-nfactors@2.3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
