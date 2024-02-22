# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpkg(RPackage):
	"""Install R Packages or Download File from GitHub via the Proxy
Site

	When you want to install R package or download file from GitHub, 
    but you can't access GitHub, this package helps you install R packages or 
    download file from GitHub via the proxy website <https://mirror.ghproxy.com/> 
    or <https://gh-proxy.com/>, which is in real-time sync with GitHub.
	"""
	
	homepage = "https://gitlab.com/chuxinyuan/ipkg"
	cran = "ipkg" 

	version("1.1.1", md5="ffb94918f0a3a7a3a32827ae7382dc93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
