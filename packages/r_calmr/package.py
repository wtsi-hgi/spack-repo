# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalmr(RPackage):
	"""Canonical Associative Learning Models and their Representations

	Implementations of canonical associative learning models, with tools to run experiment simulations, estimate model parameters, and compare model representations. Experiments and results are represented using S4 classes and methods.
	"""
	
	homepage = "https://github.com/victor-navarro/calmr"
	cran = "calmr" 

	version("0.6.1", md5="1057d4bd912c4d8db4c6b8a49646d082")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
