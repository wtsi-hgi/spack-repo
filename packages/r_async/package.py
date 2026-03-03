# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsync(RPackage):
	"""Coroutines: Generators / Yield, Async / Await, and Streams

	Write sequential-looking code that pauses and resumes.
             gen() creates a generator, an iterator that returns a
             value and pauses each time it reaches a yield() call.
             async() creates a promise, which runs until it reaches
             a call to await(), then resumes when information is available.
             These work similarly to generator and async constructs
             from 'Python' or 'JavaScript'. Objects produced are
             compatible with the 'iterators' and 'promises' packages.
             Version 0.3 supports on.exit, single-step debugging,
             stream() for making asynchronous iterators, and
             delimited goto() in switch() calls.
	"""
	
	homepage = "https://crowding.github.io/async/"
	cran = "async" 

	version("0.3.2", md5="c222a8bb55940a46264ab22f67210596")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-iterors", type=("build", "run"))
	depends_on("r-nseval@0.4.3:", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
