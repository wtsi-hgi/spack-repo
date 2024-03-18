# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsclient(RPackage):
	"""Client for Rserve

	Client for Rserve, allowing to connect to Rserve instances and issue commands.
	"""
	
	homepage = "http://www.rforge.net/RSclient/"
	cran = "RSclient" 

	version("0.7-10", md5="6bfd1f836d6be98e75b4bbd0f7cbb521")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("openssl", type=("build", "link", "run"))
