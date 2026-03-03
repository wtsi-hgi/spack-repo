# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscrtr(RPackage):
	"""A Companion Package for the Book "Discrete Choice Analysis with
'R'"

	Templates and data files to support "Discrete Choice Analysis with R",
    Páez, A. and Boisjoly, G. (2023) <doi:10.1007/978-3-031-20719-8>.
	"""
	
	homepage = "https://github.com/paezha/discrtr"
	cran = "discrtr" 

	version("0.0.1", md5="0936d9e4fb02a72e94eb6fb8c7ef0e4d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rmdformats", type=("build", "run"))
