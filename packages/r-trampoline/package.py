# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrampoline(RPackage):
	"""Make Functions that Can Recurse Infinitely

	Implements a trampoline algorithm for R that let's users write recursive functions
    that get around R's stack call limitations, enabling theoretically infinite recursion. The
    algorithm is based around generator function as implemented in the 'coro' package, and is
    based almost completely on the 'trampoline' module from Python <https://gitlab.com/ferreum/trampoline>.
	"""
	
	homepage = "https://github.com/rdinnager/trampoline"
	cran = "trampoline" 

	version("0.1.1", md5="913254cd381fef0a9976c22aa8168932")

	depends_on("r-coro", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
