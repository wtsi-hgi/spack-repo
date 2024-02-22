# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBabsimHospital(RPackage):
	"""Bartz & Bartz Simulation Hospital

	Implements a discrete-event simulation model for a hospital resource planning problem.
    The project is motivated by the challenges faced by health care institutions in the current COVID-19 pandemic. 
    It can be used by health departments to forecast demand for intensive care beds, ventilators, and staff resources.
    Our modelling approach is inspired by "A novel modelling technique to predict resource requirements in critical care - a case study" (Lawton and McCooe 2019) and combines two powerful technologies: 
      (i) discrete event simulation using the 'simmer' package and 
      (ii) model-based optimization using 'SPOT'.
    Ucar I, Smeets B, Azcorra A (2019) <doi:10.18637/jss.v090.i02>.
    Bartz-Beielstein T, Lasarczyk C W G, Preuss M (2005) <doi:10.1109/CEC.2005.1554761>.
    Lawton T, McCooe M (2019) <doi:10.7861/futurehosp.6-1-17>.
	"""
	
	homepage = "https://www.th-koeln.de/babsimhospital"
	cran = "babsim.hospital" 

	version("11.8.8", md5="83d8d972b42e5d9b2758b85acb1b915c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-spot", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-markovchain", type=("build", "run"))
	depends_on("r-padr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-simmer", type=("build", "run"))
	depends_on("r-slider", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
