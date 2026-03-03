# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSocialmixr(RPackage):
	"""Social Mixing Matrices for Infectious Disease Modelling

	Provides methods for sampling contact matrices from diary
    data for use in infectious disease modelling, as discussed in Mossong
    et al. (2008) <doi:10.1371/journal.pmed.0050074>.
	"""
	
	homepage = "https://github.com/epiforecasts/socialmixr"
	cran = "socialmixr" 

	version("0.3.1", md5="6e0084a645a03f00c9ef8493796e965e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-oai", type=("build", "run"))
	depends_on("r-wpp2017", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
