# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRilostat(RPackage):
	"""ILO Open Data via Ilostat Bulk Download Facility

	Tools to download data from the ilostat database
    <https://ilostat.ilo.org> together with search and
    manipulation utilities.
	"""
	
	homepage = "https://ilostat.github.io/Rilostat/"
	cran = "Rilostat" 

	version("2.0.0", md5="30962a8fb2bfb5d531d745df302678a4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-readr@2.1.4:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
