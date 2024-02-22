# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaptr(RPackage):
	"""Client for the Captricity API

	Get text from images of text using Captricity Optical Character
    Recognition (OCR) API. Captricity allows you to get text from handwritten
    forms --- think surveys --- and other structured paper documents. And it can
    output data in form a delimited file keeping field information intact. For more
    information, read <https://shreddr.captricity.com/developer/overview/>.
	"""
	
	homepage = "http://github.com/soodoku/captR"
	cran = "captr" 

	version("0.3.0", md5="28e6c0244e42b819dc49cc29c1d075f9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
