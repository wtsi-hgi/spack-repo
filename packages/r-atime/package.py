# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtime(RPackage):
	"""Asymptotic Timing

	Computing and visualizing comparative
 asymptotic timings of different algorithms and code versions.
 Also includes functionality for comparing empirical timings with
 expected references such as linear or quadratic,
 <https://en.wikipedia.org/wiki/Asymptotic_computational_complexity>
 Also includes functionality for measuring asymptotic memory and other
 quantities.
	"""
	
	homepage = "https://github.com/tdhock/atime"
	cran = "atime" 

	version("2024.1.31", md5="5a0397b7dee96c560de690c4f5f8b180")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bench", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
