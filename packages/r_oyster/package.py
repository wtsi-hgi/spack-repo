# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROyster(RPackage):
	"""Scans R Projects for Vulnerable Third Party Dependencies

	Collects a list of your third party R packages, and
    scans them with the 'OSS' Index provided by 'Sonatype', reporting back
    on any vulnerabilities that are found in the third party packages you
    use.
	"""
	
	homepage = "https://github.com/sonatype-nexus-community/oysteR"
	cran = "oysteR" 

	version("0.1.1", md5="bba7f699369e25f553b098ca41bdcd6f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
