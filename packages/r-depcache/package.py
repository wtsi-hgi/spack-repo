# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepcache(RPackage):
	"""Cache R Expressions, Taking Their Dependencies into Account

	Hash an expression with its dependencies and store its
	value, reloading it from a file as long as both the expression and
	its dependencies stay the same.
	"""
	
	cran = "depcache" 

	version("0.1-2", md5="7bbc8fa0f42e0f0ef8b4185ad8109124")

	depends_on("r-codetools", type=("build", "run"))
