# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterator(RPackage):
	"""Print Loop Iterations at Exponentially Disparate Intervals

	Know which loop iteration the code execution is up to by including
    a single, convenient function call inside the loop.
	"""
	
	homepage = "https://github.com/stevecondylios/iteratoR"
	cran = "iteratoR" 

	version("0.1.1", md5="9e1ff3c0eb97471fcb6925e58e6919d3")

