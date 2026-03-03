# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApacheSedona(RPackage):
	"""R Interface for Apache Sedona

	R interface for 'Apache Sedona' based on 'sparklyr'
	(<https://sedona.apache.org>).
	"""
	
	homepage = "https://github.com/apache/sedona/"
	cran = "apache.sedona"

	version("1.5.1", md5="45318ee0c148ba1963fdc4d1f8b4979e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sparklyr@1.3:", type=("build", "run"))
	depends_on("r-dbplyr@1.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("spark", type=("build", "link", "run"))
