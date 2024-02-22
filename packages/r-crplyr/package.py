# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrplyr(RPackage):
	"""A 'dplyr' Interface for Crunch

	In order to facilitate analysis of datasets hosted on the Crunch
    data platform <https://crunch.io/>, the 'crplyr' package implements 'dplyr'
    methods on top of the Crunch backend. The usual methods 'select', 'filter',
    'group_by', 'summarize', and 'collect' are implemented in such a way as to
    perform as much computation on the server and pull as little data locally
    as possible.
	"""
	
	homepage = "https://crunch.io/r/crplyr/"
	cran = "crplyr" 

	version("0.4.0", md5="534afdfeb10a8dd32ff2eb86f7b65202")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-crunch@1.15.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httptest@3:", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
