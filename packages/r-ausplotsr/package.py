# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAusplotsr(RPackage):
	"""TERN AusPlots Australian Ecosystem Monitoring Data

	Extraction, preparation, visualisation and analysis of TERN AusPlots ecosystem monitoring data. Direct access to plot-based data on vegetation and soils across Australia, including physical sample barcode numbers. Simple function calls extract the data and merge them into species occurrence matrices for downstream analysis, or calculate things like basal area and fractional cover. TERN AusPlots is a national field plot-based ecosystem surveillance monitoring method and dataset for Australia. The data have been collected across a national network of plots and transects by the Terrestrial Ecosystem Research Network (TERN - <https://www.tern.org.au>), an Australian Government NCRIS-enabled project, and its Ecosystem Surveillance platform (<https://www.tern.org.au/tern-land-observatory/ecosystem-surveillance-and-environmental-monitoring/>).
	"""
	
	cran = "ausplotsR" 

	version("2.0.5", md5="251e536a227a1901a3f9472a6027c488")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mapdata", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
	depends_on("r-betapart", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-r2r", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
