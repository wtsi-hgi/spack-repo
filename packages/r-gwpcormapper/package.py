# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwpcormapper(RPackage):
	"""Geographically Weighted Partial Correlation Mapper

	An interactive mapping tool for geographically weighted correlation and partial correlation. Geographically weighted partial correlation coefficients are calculated following (Percival and Tsutsumida, 2017)<doi:10.1553/giscience2017_01_s36> and are described in greater detail in (Tsutsumida et al., 2019)<doi:10.5194/ica-abs-1-372-2019> and (Percival et al., 2021)<arXiv:2101.03491>.
	"""
	
	homepage = "https://github.com/gwpcor/gwpcormapper"
	cran = "gwpcormapper" 

	version("0.1.3", md5="a919f8a96e5936760fcf9713e1b520bc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
