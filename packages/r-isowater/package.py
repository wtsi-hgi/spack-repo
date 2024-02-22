# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsowater(RPackage):
	"""Discovery, Retrieval, and Analysis of Water Isotope Data

	The wiDB...() functions provide an interface to the public API 
    of the wiDB <https://github.com/SPATIAL-Lab/isoWater/blob/master/Protocol.md>: 
    build, check and submit queries, and receive and 
    unpack responses. Data analysis functions support Bayesian 
    inference of the source and source isotope composition of water 
    samples that may have experienced evaporation. Algorithms 
    adapted from Bowen et al. (2018, <doi:10.1007/s00442-018-4192-5>).
	"""
	
	cran = "isoWater" 

	version("1.1.2", md5="6907d0c471b663d8b3a9a4fe6be3a3a6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-r2winbugs", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
