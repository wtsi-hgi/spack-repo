# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRProxy(RPackage):
	"""Set Proxy in R Console

	The use of proxies is required in certain network
    environments.  Despite the power of system level software, it is still
    inconvenient to switch proxy networks at random in R's console. This
    package is designed to provide one-click switching between proxy and
    non-proxy states.
	"""
	
	homepage = "https://github.com/xiayh17/r.proxy"
	cran = "r.proxy" 

	version("0.1.3", md5="b582a815fe066961ab73347dcd96a19b")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
