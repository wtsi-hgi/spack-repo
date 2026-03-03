# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBc3net(RPackage):
	"""Gene Regulatory Network Inference with Bc3net

	Implementation of the BC3NET algorithm for gene regulatory network inference (de Matos Simoes and Frank Emmert-Streib, Bagging Statistical Network Inference from Large-Scale Gene Expression Data, PLoS ONE 7(3): e33624, <doi:10.1371/journal.pone.0033624>).
	"""
	
	cran = "bc3net" 

	version("1.0.4", md5="7c0a1c5328cee7b18c649a99001763f4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-c3net", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
