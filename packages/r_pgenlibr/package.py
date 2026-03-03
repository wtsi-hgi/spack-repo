# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgenlibr(RPackage):
	"""PLINK 2 Binary (.pgen) Reader

	A thin wrapper over PLINK 2's core libraries which provides an R
    interface for reading .pgen files.  A minimal .pvar loader is also
    included.  Chang et al. (2015) <doi:10.1186/s13742-015-0047-8>.
	"""
	
	cran = "pgenlibr" 

	version("0.3.5", md5="843d9f1210f252a095942fa51e5dd16b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
