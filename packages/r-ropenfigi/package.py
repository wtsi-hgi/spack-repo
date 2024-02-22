# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopenfigi(RPackage):
	"""R Interface to OpenFIGI

	Provide a simple interface to Bloomberg's OpenFIGI API. Please
    see <https://openfigi.com> for API details and registration. You may be
    eligible to have an API key to accelerate your loading process.
	"""
	
	homepage = "https://github.com/HuangRicky/ROpenFIGI"
	cran = "ROpenFIGI" 

	version("0.2.8", md5="6e9a03a7837f05766d635267d6ca0177")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
