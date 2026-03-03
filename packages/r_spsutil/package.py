# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpsutil(RPackage):
	"""'systemPipeShiny' Utility Functions

	The systemPipeShiny (SPS) framework comes with many useful utility functions. However, installing the whole framework is heavy and takes some time. If you like only a few useful utility functions from SPS, install this package is enough.
	"""
	
	homepage = "https://github.com/lz100/spsUtil"
	cran = "spsUtil" 

	version("0.2.2", md5="d67271e88f168140249b3e05f66c2d1e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
