# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbp(RPackage):
	"""Wrapper for the National Bank of Poland API

	Use the <http://api.nbp.pl/> API through R. Retrieve
    currency exchange rates and gold prices data published by the
    National Bank of Poland in form of convenient R objects.
	"""
	
	cran = "rnbp" 

	version("0.2.1", md5="0654416b13782e5329bc4deb8facfcde")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
