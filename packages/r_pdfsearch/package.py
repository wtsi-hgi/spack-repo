# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdfsearch(RPackage):
	"""Search Tools for PDF Files

	Includes functions for keyword search of pdf files. There is
    also a wrapper that includes searching of all files within a single
    directory.
	"""
	
	homepage = "https://github.com/lebebr01/pdfsearch"
	cran = "pdfsearch" 

	version("0.3.0", md5="915ceb0f6ba4f7d2c94f2af6e44f7286")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
