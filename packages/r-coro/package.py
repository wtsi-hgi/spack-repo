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

	version("1.0.4", sha256="9c9aa7c4d659794c4440ec19e3d436b7da6a60a9ea5cd142a50c790546bea4b2")
	version("1.0.3", sha256="4e7729b1b1461be7805b2fcad0ed4c04755390dad3f1a2cb9f3af701db6d7d73")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.12:", type=("build", "run"))
