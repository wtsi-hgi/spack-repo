# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RPdftools(RPackage):
	"""Text Extraction, Rendering and Converting of PDF Documents

	Utilities based on 'libpoppler' for extracting text, fonts, attachments and 
    metadata from a PDF file. Also supports high quality rendering of PDF documents into
    PNG, JPEG, TIFF format, or into raw bitmap vectors for further processing in R.
	"""
	
	homepage = "https://docs.ropensci.org/pdftools/"
	cran = "pdftools" 

	version("3.4.0", md5="b0cdb2d649557b5902e81a8e9e215eb5")

	depends_on("r-rcpp@0.12.12:", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("poppler+cpp", type=("build", "link"))
	depends_on("pkg-config", type=("build", "link"))
