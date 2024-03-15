# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCachem(RPackage):
	"""Cache R Objects with Automatic Pruning.

	Key-value stores with automatic pruning. Caches can limit either their
	total size or the age of the oldest object (or both), automatically pruning
	objects to maintain the constraints."""

	cran = "cachem"

	license("MIT")

	version("1.0.8", md5="f7b8c1dae009101e6785febca66bb659")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-fastmap@1.1.1:", type=("build", "run"))
