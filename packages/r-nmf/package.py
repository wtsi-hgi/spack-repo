# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmf(RPackage):
	"""Algorithms and Framework for Nonnegative Matrix Factorization (NMF).

	Provides a framework to perform Non-negative Matrix Factorization (NMF).
	The package implements a set of already published algorithms and seeding
	methods, and provides a framework to test, develop and plug new/custom
	algorithms. Most of the built-in algorithms have been optimized in C++, and
	the main interface function provides an easy way of performing parallel
	computations on multicore machines."""

	cran = "NMF"

	version("0.27", md5="1b529cab49a1f0cf8d8b1c83a4f38229")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-registry", type=("build", "run"))
	depends_on("r-rngtools@1.2.3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
