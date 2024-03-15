# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpwshiftr(RPackage):
	"""Create Future 'EnergyPlus' Weather Files using 'CMIP6' Data

	
    Query, download climate change projection data from the 'CMIP6' (Coupled
    Model Intercomparison Project Phase 6) project
    <https://pcmdi.llnl.gov/CMIP6/> in the 'ESGF' (Earth System Grid Federation)
    platform <https://esgf.llnl.gov>, and create future 'EnergyPlus'
    <https://energyplus.net> Weather ('EPW') files adjusted from climate changes
    using data from Global Climate Models ('GCM').
	"""
	
	homepage = "https://github.com/ideas-lab-nus/epwshiftr"
	cran = "epwshiftr" 

	version("0.1.4", md5="566ed863407618e11ded8e6451cf990a")

	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-eplusr@0.15.2:", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pcict", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-psychrolib", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rnetcdf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
