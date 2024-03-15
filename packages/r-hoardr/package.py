# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHoardr(RPackage):
	"""Manage Cached Files.

	Suite of tools for managing cached files, targeting use in other R
	packages. Uses 'rappdirs' for cross-platform paths. Provides utilities to
	manage cache directories, including targeting files by path or by key;
	cached directories can be compressed and uncompressed easily to save disk
	space."""

	cran = "hoardr"

	license("MIT")

	version("0.5.4", md5="5e6a6d4bc14435aed449fddda3dacf19")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
