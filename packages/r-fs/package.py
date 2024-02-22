# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFs(RPackage):
	"""Cross-Platform File System Operations Based on 'libuv'.

	A cross-platform interface to file system operations, built on top of the
	'libuv' C library."""

	cran = "fs"

	version("1.6.3", md5="25dc9b509f6a8fba2718ffd2c691124a")

	depends_on("r@3.4:", type=("build", "run"))
