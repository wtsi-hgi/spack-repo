# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGensa(RPackage):
	"""Generalized Simulated Annealing.

	Performs search for global minimum of a very complex non-linear objective
	function with a very large number of optima."""

	cran = "GenSA"

	version("1.1.14", md5="9fa83600929fd3bf4a42a8501c32d478")

	depends_on("r@2.12:", type=("build", "run"))
