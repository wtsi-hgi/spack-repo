# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtt(RPackage):
	"""The Table Tool

	Create structured, formatted HTML tables of in a flexible and
    convenient way.
	"""
	
	homepage = "https://github.com/benjaminrich/ttt"
	cran = "ttt" 

	version("1.0", md5="823cea1c356d765f7a15fa39ee4e414f")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
