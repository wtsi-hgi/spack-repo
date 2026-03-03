# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvhttp(RPackage):
	"""'SciViews' - HTTP Server

	A simple HTTP server allows to connect GUI clients to R.
	"""
	
	homepage = "https://github.com/SciViews/svHttp"
	cran = "svHttp" 

	version("1.0.4", md5="b170aff68245c0c29ebf4e014517f8e6")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-svmisc@0.9.68:", type=("build", "run"))
