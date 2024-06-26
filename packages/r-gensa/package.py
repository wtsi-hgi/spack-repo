# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGensa(RPackage):
	"""Generalized Simulated Annealing.

	Performs search for global minimum of a very complex non-linear objective
	function with a very large number of optima."""

	cran = "GenSA"
	version("1.1.8", sha256="375e87541eb6b098584afccab361dc28ff09d03cf1d062ff970208e294eca216")
	version("1.1.7", sha256="9d99d3d0a4b7770c3c3a6de44206811272d78ab94481713a8c369f7d6ae7b80f")
	version("1.1.14", md5="9fa83600929fd3bf4a42a8501c32d478")

	depends_on("r@2.12:", type=("build", "run"))
