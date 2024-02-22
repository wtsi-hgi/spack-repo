# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVietnameseconverter(RPackage):
	"""Convert Vietnamese Encodings

	Conversion of characters from unsupported Vietnamese character encodings to Unicode characters. These Vietnamese encodings (TCVN3, VISCII, VPS) are not natively supported in R and lead to printing of wrong characters and garbled text (mojibake). This package fixes that problem and provides readable output with the correct Unicode characters (with or without diacritics). 
	"""
	
	homepage = "https://github.com/jniedballa/vietnameseConverter"
	cran = "vietnameseConverter" 

	version("0.4.0", md5="55c96f679e4da0cfc29a7daf71d21935")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
