# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcessd(RPackage):
	"""Stock Database Web Services

	R interface to access the web services of the ICES Stock Database <https://sd.ices.dk>.
	"""
	
	homepage = "https://sd.ices.dk"
	cran = "icesSD" 

	version("2.0.0", md5="016d1786026c1caacde62693da6af2fe")

	depends_on("r-icesconnect@1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
