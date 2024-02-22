# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeaval(RPackage):
	"""Validation of Seasonal Weather Forecasts

	Provides tools for processing and evaluating seasonal weather forecasts, 
    with an emphasis on tercile forecasts. We follow the World Meteorological Organization's 
    "Guidance on Verification of Operational Seasonal Climate Forecasts", 
    S.J.Mason (2018, ISBN: 978-92-63-11220-0, URL: <https://library.wmo.int/idurl/4/56227>). 
    The development was supported by the European Union’s Horizon 2020 research and innovation 
    programme under grant agreement no. 869730 (CONFER).
    A comprehensive online tutorial is available at <http://files.nr.no/samba/CONFER/SeaVal/>.
	"""
	
	homepage = "http://files.nr.no/samba/CONFER/SeaVal/"
	cran = "SeaVal" 

	version("1.1.1", md5="3bdeebffae3f3f8af8c985d176304a4b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
