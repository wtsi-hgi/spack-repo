# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNesrdata(RPackage):
	"""National Eutrophication Survey Data

	Serves data from the United States Environmental Protection Agency (USEPA) National Eutrophication Survey <https://www.epa.gov/national-aquatic-resource-surveys>.
	"""
	
	homepage = "https://github.com/jsta/nesRdata"
	cran = "nesRdata" 

	version("0.3.1", md5="20299ecb1ee8628321d00e8593327f28")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dataone", type=("build", "run"))
