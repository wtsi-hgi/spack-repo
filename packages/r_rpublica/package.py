# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpublica(RPackage):
	"""ProPublica API Client

	Client for accessing data journalism APIs from ProPublica <http://www.propublica.org/>.
	"""
	
	homepage = "https://github.com/rOpenGov/RPublica"
	cran = "RPublica" 

	version("0.1.3", md5="3828aabca98143d1a6b74a098037a224")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
