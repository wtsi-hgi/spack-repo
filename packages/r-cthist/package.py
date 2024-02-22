# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCthist(RPackage):
	"""Clinical Trial Registry History

	Retrieves historical versions of clinical trial registry
    entries from <https://ClinicalTrials.gov>. Package functionality
    and implementation for v 1.0.0 is documented in Carlisle (2022)
    <DOI:10.1371/journal.pone.0270909>.
	"""
	
	homepage = "https://github.com/bgcarlisle/cthist"
	cran = "cthist" 

	version("2.1.6", md5="4dd2a34dc67596e2237c3971dbaf6423")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
