# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListcomp(RPackage):
	"""List Comprehensions

	An implementation of list comprehensions as purely syntactic
  sugar with a minor runtime overhead. It constructs nested for-loops and
  executes the byte-compiled loops to collect the results.
	"""
	
	homepage = "https://github.com/dirkschumacher/listcomp"
	cran = "listcomp" 

	version("0.4.1", md5="ad24808b8ebbd1d7952c08c39b1858ff")

	depends_on("r-rlang", type=("build", "run"))
