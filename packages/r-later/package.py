# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLater(RPackage):
	"""Utilities for Scheduling Functions to Execute Later with Event Loops.

	Executes arbitrary R or C functions some time after the current time, after
	the R execution stack has emptied."""

	cran = "later"

	license("MIT")

	version("1.3.2", md5="d051b4ebe4f306287003877aae5ab95c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
