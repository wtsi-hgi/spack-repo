# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMathpix(RPackage):
	"""Support for the 'Mathpix' API (Image to 'LaTeX')

	Given an image of a formula (typeset or handwritten) this package
    provides calls to the 'Mathpix' service to produce the 'LaTeX' code which should
    generate that image, and pastes it into a (e.g. an 'rmarkdown') document. 
    See <https://docs.mathpix.com/> for full details. 'Mathpix' is an external service 
    and use of the API is subject to their terms and conditions.
	"""
	
	homepage = "https://github.com/jonocarroll/mathpix"
	cran = "mathpix" 

	version("0.6.0", md5="71e95ae49f2323fa5db741f7fb1a107e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
