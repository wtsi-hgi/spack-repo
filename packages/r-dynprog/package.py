# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynprog(RPackage):
	"""Dynamic Programming Domain-Specific Language

	A domain-specific language for specifying translating recursions
    into dynamic-programming algorithms. See 
    <https://en.wikipedia.org/wiki/Dynamic_programming> for a description
    of dynamic programming.
	"""
	
	homepage = "https://github.com/mailund/dynprog"
	cran = "dynprog" 

	version("0.1.1", md5="116df0abc341ce6952aed8fe4e94f434")

	depends_on("r-rlang@0.1.2:", type=("build", "run"))
