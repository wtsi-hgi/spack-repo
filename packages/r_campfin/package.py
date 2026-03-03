# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCampfin(RPackage):
	"""Wrangle Campaign Finance Data

	Explore and normalize American campaign finance
    data. Created by the Investigative Reporting Workshop to facilitate
    work on The Accountability Project, an effort to collect public data
    into a central, standard database that is more easily searched:
    <https://publicaccountability.org/>.
	"""
	
	homepage = "https://github.com/irworkshop/campfin"
	cran = "campfin" 

	version("1.0.11", md5="dc36afb0d94cd01bf9a81a524a50973e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-fs@1.3.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-stringdist@0.9.5.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
