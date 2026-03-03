# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChunked(RPackage):
	"""Chunkwise Text-File Processing for 'dplyr'

	Data stored in text file can be processed chunkwise using 'dplyr' commands. These
    are recorded and executed per data chunk, so large files can be processed with
    limited memory using the 'LaF' package.
	"""
	
	homepage = "https://github.com/edwindj/chunked"
	cran = "chunked" 

	version("0.6.0", md5="6cc81ae6deed4736fcbe12c6cc5936c3")

	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-laf", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
