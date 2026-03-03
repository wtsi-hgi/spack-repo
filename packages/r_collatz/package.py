# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollatz(RPackage):
	"""Functions Related to the Collatz/Syracuse/3n+1 Problem

	Provides the basic functionality to interact with the Collatz conjecture.
    The parameterisation uses the same (P,a,b) notation as Conway's generalisations.
    Besides the function and reverse function, there is also functionality to retrieve
    the hailstone sequence, the "stopping time"/"total stopping time", or tree-graph. 
    The only restriction placed on parameters is that both P and a can't be 0.
    For further reading, see <https://en.wikipedia.org/wiki/Collatz_conjecture>.
	"""
	
	homepage = "https://github.com/Skenvy/Collatz"
	cran = "collatz" 

	version("1.0.0", md5="6b07f131c0d839d7b2856f9eed298a82")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
