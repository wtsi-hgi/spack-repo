# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatelimitr(RPackage):
	"""Rate Limiting for R

	Allows to limit the rate at which one or more functions can be called.
	"""
	
	homepage = "https://github.com/tarakc02/ratelimitr"
	cran = "ratelimitr" 

	version("0.4.1", md5="ad6c3c861a29eb9c0b0ad3820f0b2050")

	depends_on("r-assertthat", type=("build", "run"))
