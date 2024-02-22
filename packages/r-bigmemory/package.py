# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigmemory(RPackage):
	"""Manage Massive Matrices with Shared Memory and Memory-Mapped.

	Files Create, store, access, and manipulate massive matrices.  Matrices are
	allocated to shared memory and may use memory-mapped files. Packages
	'biganalytics', 'bigtabulate', 'synchronicity', and 'bigalgebra' provide
	advanced functionality."""

	cran = "bigmemory"

	version("4.6.4", md5="6b58104bfb99f48c0ff3b26c6f6fc441")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-bigmemory-sri", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-uuid@1.0.2:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
