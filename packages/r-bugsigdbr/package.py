# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBugsigdbr(RPackage):
	"""R-side access to published microbial signatures from BugSigDB

	The bugsigdbr package implements convenient access to bugsigdb.org from within R/Bioconductor. The goal of the package is to facilitate import of BugSigDB data into R/Bioconductor, provide utilities for extracting microbe signatures, and enable export of the extracted signatures to plain text files in standard file formats such as GMT.
	"""
	
	homepage = "https://github.com/waldronlab/bugsigdbr"
	bioc = "bugsigdbr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bugsigdbr_1.8.4.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bugsigdbr/bugsigdbr_1.8.4.tar.gz"]

	version("1.8.4", md5="faa6fc9f619e17f958ff116ee748e84c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
