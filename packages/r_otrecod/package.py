# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtrecod(RPackage):
	"""Data Fusion using Optimal Transportation Theory

	In the context of data fusion, the package provides a set of functions dedicated to the solving of 'recoding problems' using optimal transportation theory (Gares, Guernec, Savy (2019) <doi:10.1515/ijb-2018-0106> and Gares, Omer (2020) <doi:10.1080/01621459.2020.1775615>). From two databases with no overlapping part except a subset of shared variables, the functions of the package assist users until obtaining a unique synthetic database, where the missing information is fully completed.
	"""
	
	cran = "OTrecod" 

	version("0.1.2", md5="8a319ba12e423d5e9996f7d3bd6208b7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-missmda", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-statmatch", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-roi-plugin-glpk", type=("build", "run"))
	depends_on("r-ompr", type=("build", "run"))
	depends_on("r-ompr-roi", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
