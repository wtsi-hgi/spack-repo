# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZip(RPackage):
	"""Cross-Platform 'zip' Compression.

	Cross-Platform 'zip' Compression Library. A replacement for the 'zip'
	function, that does not require any additional external tools on any
	platform."""

	cran = "zip"

	version("2.3.1", md5="8a8a132cd0456e498d479d21c91facce")

