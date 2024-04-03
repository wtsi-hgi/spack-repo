# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpdf(RPackage):
	"""Split, Combine and Compress PDF Files

	Content-preserving transformations transformations of PDF files such 
    as split, combine, and compress. This package interfaces directly to the 'qpdf' 
    C++ API and does not require any command line utilities. Note that 'qpdf' does
    not read actual content from PDF files: to extract text and data you need the
    'pdftools' package.
	"""
	
	homepage = "https://docs.ropensci.org/qpdf/"
	cran = "qpdf" 

	version("1.3.3", md5="befda010dc47d87b6e988db7d6941768")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
