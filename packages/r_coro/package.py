# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoro(RPackage):
	"""'Coroutines' for R

	Provides 'coroutines' for R, a family of functions that can
    be suspended and resumed later on. This includes 'async' functions
    (which await) and generators (which yield). 'Async' functions are
    based on the concurrency framework of the 'promises' package.
    Generators are based on a dependency free iteration protocol defined
    in 'coro' and are compatible with iterators from the 'reticulate'
    package.
	"""
	
	homepage = "https://github.com/r-lib/coro"
	cran = "coro" 

	version("1.0.4", md5="20d535e6d36920c23c8e74442977806a")
	version("1.0.3", md5="62deada3e82a20ea35fe9fb86cc98506")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.12:", type=("build", "run"))
