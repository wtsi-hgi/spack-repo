# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLobstr(RPackage):
	"""Visualize R Data Structures with Trees.

	A set of tools for inspecting and understanding R data structures inspired
	by str(). Includes ast() for visualizing abstract syntax trees, ref() for
	showing shared references, cst() for showing call stack trees, and
	obj_size() for computing object sizes."""

	cran = "lobstr"

	license("MIT")

	version("1.1.2", md5="742ca7fe19f22d6d8246e6d5696b70f5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-cpp11@0.4.2:", type=("build", "run"))
