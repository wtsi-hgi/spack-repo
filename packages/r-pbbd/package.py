# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbbd(RPackage):
	"""Position Balanced and Nearly Position Balanced Block Designs

	Generates a position balanced or nearly position balanced block design with given parameters.  This package can also convert a given proper and equireplicate block design into a position balanced or nearly position balanced block design.
	"""
	
	cran = "pbbd" 

	version("1.0.0", md5="014e196b84df62020e9cd6346eef9e34")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ibd@1.5:", type=("build", "run"))
