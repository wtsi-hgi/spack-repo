# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBindrcpp(RPackage):
	"""An 'Rcpp' Interface to Active Bindings.

	Provides an easy way to fill an environment with active bindings that call
	a C++ function."""

	cran = "bindrcpp"

	license("MIT")

	version("0.2.3", md5="14d52a9f59269bc1a674bb1e93abdfda")

	depends_on("r-bindr@0.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plogr", type=("build", "run"))
