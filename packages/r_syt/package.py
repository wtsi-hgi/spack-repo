# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyt(RPackage):
	"""Standard Young Tableaux

	Deals with standard Young tableaux (field of combinatorics).
    Performs enumeration, counting, random generation, the
    Robinson-Schensted correspondence, and conversion to and from paths on
    the Young lattice. Also performs enumeration and counting of 
    semistandard Young tableaux.
	"""
	
	homepage = "https://github.com/stla/syt"
	cran = "syt" 

	version("0.3.0", md5="6c2b0fc29fb3a2c899a4679d0dc9484e")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
