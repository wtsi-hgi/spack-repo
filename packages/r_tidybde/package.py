# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidybde(RPackage):
	"""Download Data from Bank of Spain

	Tools to download data series from 'Banco de España' ('BdE')
    on 'tibble' format. 'Banco de España' is the national central bank
    and, within the framework of the Single Supervisory Mechanism ('SSM'),
    the supervisor of the Spanish banking system along with the European
    Central Bank. This package is in no way sponsored endorsed or
    administered by 'Banco de España'.
	"""
	
	homepage = "https://ropenspain.github.io/tidyBdE/"
	cran = "tidyBdE" 

	version("0.3.5", md5="31ac054360192427d562123326572314")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-readr@1:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
