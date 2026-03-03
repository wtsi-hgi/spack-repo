# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpinterest(RPackage):
	"""Access Pinterest API

	Get information (boards, pins and
    users) from the Pinterest <http://www.pinterest.com>
    API.
	"""
	
	cran = "rpinterest" 

	version("0.3.1", md5="5da69950ded857d9aaaf0080df1c6125")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
