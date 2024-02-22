# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcp(RPackage):
	"""Function Composition

	A function composition operator to chain a series of calls into a single function, mimicking the math notion of (f o g o h)(x) = h(g(f(x))). Inspired by 'pipeOp' ('|>') since R4.1 and 'magrittr pipe' ('%>%'), the operator build a pipe without putting data through, which is best for anonymous function accepted by utilities such as apply() and lapply().
	"""
	
	homepage = "https://github.com/xiaoran831213/R_fun_comp"
	cran = "fcp" 

	version("0.1.0", md5="6ce4ba135b7d8f44568d7463f01edb19")

	depends_on("r@3.5:", type=("build", "run"))
