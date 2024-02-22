# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMskccOncotree(RPackage):
	"""Interface to the 'OncoTree' API

	Programmatic access to 'OncoTree' API
    <http://oncotree.mskcc.org/>. Get access to tumor main types, identifiers
    and utility routines to map across to other tumor classification systems.
	"""
	
	homepage = "https://maialab.org/mskcc.oncotree/"
	cran = "mskcc.oncotree" 

	version("0.1.1", md5="dcf5656abc45e3de05f38a7d0808d423")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyjson", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
