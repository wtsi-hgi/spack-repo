# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopenblas(RPackage):
	"""Download, Compile and Link 'OpenBLAS' Library with R

	The 'ropenblas' package (<https://prdm0.github.io/ropenblas/>) is useful for users of any 'GNU/Linux' distribution. It will be possible to download, compile and link the 'OpenBLAS' library (<https://www.openblas.net/>) with the R language, always by the same procedure, regardless of the 'GNU/Linux' distribution used. With the 'ropenblas' package it is possible to download, compile and link the latest version of the 'OpenBLAS' library even the repositories of the 'GNU/Linux' distribution used do not include the latest versions of 'OpenBLAS'. If of interest, older versions of the 'OpenBLAS' library may be considered. Linking R with an optimized version of 'BLAS' (<https://netlib.org/blas/>) may improve the computational performance of R code. The 'OpenBLAS' library is an optimized implementation of 'BLAS' that can be easily linked to R with the 'ropenblas' package.    
	"""
	
	homepage = "https://prdm0.github.io/ropenblas/"
	cran = "ropenblas" 

	version("0.3.0", md5="f8865fae310d955073e9ce563e9b2cb5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("gcc", type=("build", "link", "run"))
