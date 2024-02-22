# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhase(RPackage):
	"""Analyse Biological Time-Series Data

	Compiles functions to trim, bin, visualise, and analyse activity/sleep time-series data collected from the Drosophila Activity Monitor (DAM) system (Trikinetics, USA). The following methods were used to compute periodograms - Chi-square periodogram: Sokolove and Bushell (1978) <doi:10.1016/0022-5193(78)90022-X>, Lomb-Scargle periodogram: Lomb (1976) <doi:10.1007/BF00648343>, Scargle (1982) <doi:10.1086/160554> and Ruf (1999) <doi:10.1076/brhm.30.2.178.1422>, and Autocorrelation: Eijzenbach et al. (1986) <doi:10.1111/j.1440-1681.1986.tb00943.x>. Identification of activity peaks is done after using a Savitzky-Golay filter (Savitzky and Golay (1964) <doi:10.1021/ac60214a047>) to smooth raw activity data. Three methods to estimate anticipation of activity are used based on the following papers - Slope method: Fernandez et al. (2020) <doi:10.1016/j.cub.2020.04.025>, Harrisingh method: Harrisingh et al. (2007) <doi:10.1523/JNEUROSCI.3680-07.2007>, and Stoleru method: Stoleru et al. (2004) <doi:10.1038/nature02926>. Rose plots and circular analysis are based on methods from - Batschelet (1981) <ISBN:0120810506> and Zar (2010) <ISBN:0321656865>.
	"""
	
	cran = "phase" 

	version("1.2.9", md5="9e18433ee55605ecba2ff72faa37c3ca")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-zeitgebr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-behavr", type=("build", "run"))
	depends_on("r-wesanderson", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
