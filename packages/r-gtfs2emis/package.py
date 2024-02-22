# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtfs2emis(RPackage):
	"""Estimating Public Transport Emissions from General Transit Feed
Specification (GTFS) Data

	A bottom up model to estimate the emission levels of public transport systems based on General Transit Feed Specification (GTFS) data. The package requires two main inputs: i) Public transport data in the GTFS standard format; and ii) Some basic information on fleet characteristics such as fleet age, technology, fuel and Euro stage. As it stands, the package estimates several pollutants at high spatial and temporal resolutions. Pollution levels can be calculated for specific transport routes, trips, time of the day or for the transport system as a whole. The output with emission estimates can be extracted in different formats, supporting analysis on how emission levels vary across space, time and by fleet characteristics. A full description of the methods used in the 'gtfs2emis' model is presented in Vieira, J. P. B.; Pereira, R. H. M.; Andrade, P. R. (2022) <doi:10.31219/osf.io/8m2cy>. 
	"""
	
	homepage = "https://ipeagit.github.io/gtfs2emis/"
	cran = "gtfs2emis" 

	version("0.1.0", md5="5e152d950b5fad5fd215da3d272c57ad")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-gtfs2gps", type=("build", "run"))
	depends_on("r-sf@0.9.0:", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
