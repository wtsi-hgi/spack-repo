# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdocumentation(RPackage):
	"""Integrate R with 'RDocumentation'

	Wraps around the default help functionality in R. Instead of plain documentation files, documentation will show up as it does on <https://www.rdocumentation.org>, a platform that shows R documentation from 'CRAN', 'GitHub' and 'Bioconductor', together with informative stats to assess the package quality.
	"""
	
	homepage = "https://www.rdocumentation.org"
	cran = "RDocumentation" 

	version("0.8.2", md5="0c8b507e78b7f8d76637b60f38ad023e")

	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-proto@0.3.10:", type=("build", "run"))
	depends_on("r-rjson@0.2.15:", type=("build", "run"))
