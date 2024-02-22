# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCppdoubles(RPackage):
	"""Fast Relative Comparisons of Floating Point Numbers in 'C++'

	Compare double-precision floating point vectors using
    relative differences. All equality operations are calculated using
    'cpp11'.
	"""
	
	cran = "cppdoubles" 

	version("0.2.0", md5="8fa61002a443563158650a1eb8fbeda1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
