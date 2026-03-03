# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDofuture(RPackage):
	"""Use Foreach to Parallelize via the Future Framework

	The 'future' package provides a unifying parallelization framework for R that supports many parallel and distributed backends. The 'foreach' package provides a powerful API for iterating over an R expression in parallel. The 'doFuture' package brings the best of the two together. There are two alternative ways to use this package. The recommended approach is to use 'y <- foreach(...) %dofuture% { ... }', which does not require using 'registerDoFuture()' and has many advantages over '%dopar%'. The alternative is the traditional 'foreach' approach by registering the 'foreach' adapter 'registerDoFuture()' and so that 'y <- foreach(...) %dopar% { ... }' runs in parallelizes with the 'future' framework.
	"""
	
	homepage = "https://doFuture.futureverse.org"
	cran = "doFuture" 

	version("1.0.1", md5="c0a531170905cf2e3cacb3d99c3e0f01")

	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-future@1.32:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-globals", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
