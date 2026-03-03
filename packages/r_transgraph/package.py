# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransgraph(RPackage):
	"""Transfer Graph Learning

	Transfer learning, aiming to use auxiliary domains to help improve learning of the target domain of interest when multiple heterogeneous datasets are available, has always been a hot topic in statistical machine learning. The recent transfer learning methods with statistical guarantees mainly focus on the overall parameter transfer for supervised models in the ideal case with the informative auxiliary domains with overall similarity. In contrast, transfer learning for unsupervised graph learning is in its infancy and largely follows the idea of overall parameter transfer as for supervised learning. 
             In this package, the transfer learning for several complex graphical models is implemented, including Tensor Gaussian graphical models, non-Gaussian directed acyclic graph (DAG), and Gaussian graphical mixture models. Notably, this package promotes local transfer at node-level and subgroup-level in DAG structural learning and Gaussian graphical mixture models, respectively, which are more flexible and robust than the existing overall parameter transfer. As by-products, transfer learning for undirected graphical model (precision matrix) via D-trace loss, transfer learning for mean vector estimation, and single non-Gaussian learning via topological layer method are also included in this package. 
             Moreover, the aggregation of auxiliary information is an important issue in transfer learning, and this package provides multiple user-friendly aggregation methods, including sample weighting, similarity weighting, and most informative selection.    
             Reference: 
             Ren, M., Zhen Y., and Wang J. (2022) <arXiv:2211.09391> "Transfer learning for tensor graphical models".    
             Ren, M., He X., and Wang J. (2023) <arXiv:2310.10239> "Structural transfer learning of non-Gaussian DAG".    
             Zhao, R., He X., and Wang J. (2022) <https://jmlr.org/papers/v23/21-1173.html> "Learning linear non-Gaussian directed acyclic graph with diverging number of nodes".
	"""
	
	cran = "TransGraph" 

	version("1.0.1", md5="e3e2e27282137e9c969763e482ee1b70")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-tlasso", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-clime", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-heteroggm", type=("build", "run"))
	depends_on("r-dcov", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-evaluationmeasures", type=("build", "run"))
