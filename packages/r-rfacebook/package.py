# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfacebook(RPackage):
	"""Access to Facebook API via R

	Provides an interface to the Facebook API.
	"""
	
	homepage = "https://github.com/pablobarbera/Rfacebook"
	cran = "Rfacebook" 

	version("0.6.15", md5="b6f7622b23cae8818c7c84dfd0a0f218")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
