# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisimpact(RPackage):
	"""Calculates Disproportionate Impact When Binary Success Data are
Disaggregated by Subgroups

	Implements methods for calculating disproportionate impact: the percentage point gap, proportionality index, and the 80% index.
 California Community Colleges Chancellor's Office (2017).  Percentage Point Gap Method. <https://www.cccco.edu/-/media/CCCCO-Website/About-Us/Divisions/Digital-Innovation-and-Infrastructure/Research/Files/PercentagePointGapMethod2017.ashx>.
 California Community Colleges Chancellor's Office (2014).  Guidelines for Measuring Disproportionate Impact in Equity Plans. <https://www.cccco.edu/-/media/CCCCO-Website/Files/DII/guidelines-for-measuring-disproportionate-impact-in-equity-plans-tfa-ada.pdf>.
	"""
	
	homepage = "https://github.com/vinhdizzo/DisImpact"
	cran = "DisImpact" 

	version("0.0.21", md5="57ebffd9bf3126d2b3ac2fd31fbcc55b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-duckdb@0.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
