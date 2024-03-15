# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromises(RPackage):
	"""Abstractions for Promise-Based Asynchronous Programming.

	Provides fundamental abstractions for doing asynchronous programming in R
	using promises. Asynchronous programming is useful for allowing a single R
	process to orchestrate multiple tasks in the background while also
	attending to something else. Semantics are similar to 'JavaScript'
	promises, but with a syntax that is idiomatic R."""

	cran = "promises"

	license("MIT")

	version("1.2.1", md5="0332949e499adeb8ede2d583d813b6c5")

	depends_on("r-fastmap@1.1:", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
