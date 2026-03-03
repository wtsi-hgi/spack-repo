# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfmem(RPackage):
	"""Simple Memory Profiling for R

	A simple and light-weight API for memory profiling of R expressions.  The profiling is built on top of R's built-in memory profiler ('utils::Rprofmem()'), which records every memory allocation done by R (also native code).
	"""
	
	homepage = "https://github.com/HenrikBengtsson/profmem"
	cran = "profmem" 

	version("0.6.0", md5="f67828b0287e8ca8d244982cc6c171e4")

