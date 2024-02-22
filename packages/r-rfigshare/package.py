# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfigshare(RPackage):
	"""An R Interface to 'figshare'

	An R interface to 'figshare'.
	"""
	
	homepage = "https://github.com/ropensci-archive/rfigshare"
	cran = "rfigshare" 

	version("0.3.8", md5="d1de17b486c2b8b9929fc74dfd125ffc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-httr@0.3:", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
