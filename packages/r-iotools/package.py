# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIotools(RPackage):
	"""I/O Tools for Streaming

	Basic I/O tools for streaming and data parsing.
	"""
	
	homepage = "https://www.rforge.net/iotools"
	cran = "iotools" 

	version("0.3-5", md5="7332d57380d833b8fe0827218d579739")

	depends_on("r@2.9:", type=("build", "run"))
