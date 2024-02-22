# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyndimred(RPackage):
	"""Dimensionality Reduction Methods in a Common Format

	
  Provides a common interface for applying dimensionality reduction methods,
  such as Principal Component Analysis ('PCA'), Independent Component Analysis ('ICA'), diffusion maps, 
  Locally-Linear Embedding ('LLE'), t-distributed Stochastic Neighbor Embedding ('t-SNE'), 
  and Uniform Manifold Approximation and Projection ('UMAP'). 
  Has built-in support for sparse matrices.
	"""
	
	homepage = "https://github.com/dynverse/dyndimred"
	cran = "dyndimred" 

	version("1.0.4", md5="338b6d6209d9cbc9375f949a736265d2")

	depends_on("r-dynutils@1.0.5:", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-lmds", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
