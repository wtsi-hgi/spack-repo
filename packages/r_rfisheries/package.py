# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfisheries(RPackage):
	"""'Programmatic Interface to the 'openfisheries.org' API'

	A programmatic interface to 'openfisheries.org'. This package is
    part of the 'rOpenSci' suite (http://ropensci.org).
	"""
	
	homepage = "http://www.github.com/ropensci/rfisheries"
	cran = "rfisheries" 

	version("0.2", md5="f0e0c4d1423d8f7382d290743fe05b2c")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
