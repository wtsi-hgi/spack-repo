# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGvc(RPackage):
	"""Global Value Chains Tools

	Several tools for Global Value Chain ('GVC') analysis are
    implemented.
	"""
	
	homepage = "https://qua.st/gvc"
	cran = "gvc" 

	version("6.4.0", md5="4a858e20035ac829173b9d00d0a0076f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-decompr", type=("build", "run"))
	depends_on("r-diagonals", type=("build", "run"))
