# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPointr(RPackage):
	"""Working Comfortably with Pointers and Shortcuts to R Objects

	R has no built-in pointer functionality. The 'pointr' package fills this gap and lets you create pointers to R objects, including subsets of dataframes. This makes your R code more readable and maintainable.
	"""
	
	homepage = "https://github.com/jsugarelli/pointr/"
	cran = "pointr" 

	version("0.2.0", md5="31fbe638333f5f1ede56a2d0d877499c")

	depends_on("r-stringr", type=("build", "run"))
