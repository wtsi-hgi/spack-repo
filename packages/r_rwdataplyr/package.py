# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwdataplyr(RPackage):
	"""Read and Manipulate Data from 'RiverWare'

	A tool to read and manipulate data generated from 'RiverWare'(TM) 
    <http://www.riverware.org/> simulations. 'RiverWare' and 'RiverSMART' 
    generate data in "rdf", "csv", and "nc" format. This package provides an 
    interface to read, aggregate, and summarize data from one or more 
    simulations in a 'dplyr' pipeline.
	"""
	
	homepage = "https://github.com/BoulderCodeHub/RWDataPlyr"
	cran = "RWDataPlyr" 

	version("0.6.4", md5="afbd88c760b9d9f795914c3d427c9e94")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-feather", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
