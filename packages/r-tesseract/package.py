# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTesseract(RPackage):
	"""Open Source OCR Engine

	Bindings to 'Tesseract': 
     a powerful optical character recognition (OCR) engine that supports over 100 languages.
     The engine is highly configurable in order to tune the detection algorithms and
     obtain the best possible results.
	"""
	
	homepage = "https://docs.ropensci.org/tesseract/"
	cran = "tesseract" 

	version("5.2.1", md5="a28794f4b8813f0d6ac0a8e871a81f9e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pdftools@1.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
