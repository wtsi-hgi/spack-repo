# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovidcast(RPackage):
	"""Client for Delphi's 'COVIDcast Epidata' API

	Tools for Delphi's 'COVIDcast Epidata' API: data access, maps and
    time series plotting, and basic signal processing. The API includes a
    collection of numerous indicators relevant to the COVID-19 pandemic in the
    United States, including official reports, de-identified aggregated medical
    claims data, large-scale surveys of symptoms and public behavior, and
    mobility data, typically updated daily and at the county level. All data
    sources are documented at
    <https://cmu-delphi.github.io/delphi-epidata/api/covidcast.html>.
	"""
	
	homepage = "https://cmu-delphi.github.io/covidcast/covidcastR/"
	cran = "covidcast" 

	version("0.5.2", md5="d9d862040f8f970f0a99b5c367613e63")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-mmwrweek", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
