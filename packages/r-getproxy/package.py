# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetproxy(RPackage):
	"""Get Free Proxy IP and Port

	Allows get address and port 
	of the free proxy server, from one of two services
	<http://gimmeproxy.com/> or <https://getproxylist.com/>. 
	And it's easy to redirect your Internet connection through
	a proxy server.
	"""
	
	homepage = "https://selesnow.github.io/getProxy/"
	cran = "getProxy" 

	version("1.13", md5="040699e652d7cf408e6cdf0f31a77ec5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
