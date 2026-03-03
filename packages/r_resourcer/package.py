# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResourcer(RPackage):
	"""Resource Resolver

	A resource represents some data or a computation unit. It is 
    described by a URL and credentials. This package proposes a Resource model
    with "resolver" and "client" classes to facilitate the access and the usage of the 
    resources.
	"""
	
	cran = "resourcer" 

	version("1.4.0", md5="54c8daa59a7b4ccc9393391dc98d27f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
