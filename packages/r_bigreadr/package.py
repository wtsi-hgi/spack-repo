# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigreadr(RPackage):
	"""Read Large Text Files

	Read large text files by splitting them in smaller files.
    Package 'bigreadr' also provides some convenient wrappers around fread()
    and fwrite() from package 'data.table'. 
	"""
	
	homepage = "https://github.com/privefl/bigreadr"
	cran = "bigreadr" 

	version("0.2.5", md5="3b1b65b9aebeda3ec4eb26eec37c3be8")

	depends_on("r-bigassertr@0.1.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
