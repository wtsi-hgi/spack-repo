# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClipr(RPackage):
	"""Read and Write from the System Clipboard.

	Simple utility functions to read from and write to the Windows, OS X, and
	X11 clipboards."""

	cran = "clipr"

	version("0.8.0", md5="558ddf145114bbc0272e6aed05b8e5fe")

