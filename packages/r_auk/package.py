# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAuk(RPackage):
	"""eBird Data Extraction and Processing in R

	Extract and process bird sightings records from
    eBird (<http://ebird.org>), an online tool for recording bird
    observations.  Public access to the full eBird database is via the
    eBird Basic Dataset (EBD; see <http://ebird.org/ebird/data/download>
    for access), a downloadable text file. This package is an interface to
    AWK for extracting data from the EBD based on taxonomic, spatial, or
    temporal filters, to produce a manageable file size that can be
    imported into R.
	"""
	
	homepage = "https://github.com/CornellLabofOrnithology/auk"
	cran = "auk" 

	version("0.7.0", md5="ece9211a340dde096884caac1ba2e7da")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-countrycode@1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
