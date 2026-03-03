# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdaprototype(RPackage):
	"""Prototype of Multiple Latent Dirichlet Allocation Runs

	Determine a Prototype from a number of runs of Latent Dirichlet Allocation (LDA) measuring its similarities with S-CLOP: A procedure to select the LDA run with highest mean pairwise similarity, which is measured by S-CLOP (Similarity of multiple sets by Clustering with Local Pruning), to all other runs. LDA runs are specified by its assignments leading to estimators for distribution parameters. Repeated runs lead to different results, which we encounter by choosing the most representative LDA run as prototype.
	"""
	
	homepage = "https://github.com/JonasRieger/ldaPrototype"
	cran = "ldaPrototype" 

	version("0.3.1", md5="826a7f4f714d4961c324395891396122")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-batchtools@0.9.11:", type=("build", "run"))
	depends_on("r-checkmate@1.8.5:", type=("build", "run"))
	depends_on("r-colorspace@1.4.1:", type=("build", "run"))
	depends_on("r-data-table@1.11.2:", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-fs@1.2:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-lda@1.4.2:", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-progress@1.1.1:", type=("build", "run"))
