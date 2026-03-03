# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRt(RPackage):
	"""Interface to the 'Request Tracker' API

	Provides a programmatic interface to the 'Request Tracker' (RT)
  HTTP API <https://rt-wiki.bestpractical.com/wiki/REST>. 'RT' is a popular
  ticket tracking system.
	"""
	
	homepage = "https://github.com/nceas/rt"
	cran = "rt" 

	version("1.1.0", md5="accc65315f352212935fde5eb3faf0a7")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
