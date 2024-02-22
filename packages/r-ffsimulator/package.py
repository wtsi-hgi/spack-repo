# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfsimulator(RPackage):
	"""Simulate Fantasy Football Seasons

	Uses bootstrap resampling to run fantasy football season
    simulations supported by historical rankings and 'nflfastR' data,
    calculating optimal lineups, and returning aggregated results.
	"""
	
	homepage = "https://ffsimulator.ffverse.com"
	cran = "ffsimulator" 

	version("1.2.3", md5="c5d7a3c53ef2271ed0fbfe486c6758a7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-ffscrapr@1.4.6:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-magrittr@1:", type=("build", "run"))
	depends_on("r-nflreadr@1.2:", type=("build", "run"))
	depends_on("r-rglpk@0.6:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-tidytable@0.6.4:", type=("build", "run"))
