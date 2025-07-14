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

	version("1.14.3", commit="6b1d99193ae750ee4a4c5d8874b450e529c58c1f")
	version("1.8.4", commit="232a3ac7b9fb3a6b78401ca2b3d7b45ddac762ab")
	version("1.8.2", md5="a6c91b6c9dd9924139fb3cf5229c2449")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
