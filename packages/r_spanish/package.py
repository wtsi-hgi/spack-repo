# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpanish(RPackage):
	"""Translate Quantities from Strings to Integer and Back. Misc
Functions on Spanish Data

	Character vector to numerical translation in Euros from Spanish
    spelled monetary quantities. Reverse translation from integer to Spanish.
    Upper limit is up to the millions range. Geocoding via Cadastral web site.
	"""
	
	homepage = "https://ropenspain.github.io/spanish/"
	cran = "spanish" 

	version("0.4.2", md5="ab95736ad08621db553ef32e261e62cd")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
