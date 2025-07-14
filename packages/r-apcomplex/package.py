# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApcomplex(RPackage):
	"""Estimate protein complex membership using AP-MS protein data

	Functions to estimate a bipartite graph of protein complex membership using AP-MS data.
	"""
	
	bioc = "apComplex"

	version("2.74.0", commit="9807e96c621ee1ba58d62e744eceb00028e58607")
	version("2.68.0", commit="f64e085ff88f473c03ed09a69299b61b3a0902a4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-org-sc-sgd-db", type=("build", "run"))
