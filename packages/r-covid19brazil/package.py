# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19brazil(RPackage):
	"""COVID-19 Dataset for Brazil

	Dataset with strategic information about COVID-19 in Brazil.
    Data for municipalities, states, region and Brazil. Data source:
    Sistema Unico de Saude - SUS.
	"""
	
	homepage = "https://github.com/alexandreloures/covid19Brazil"
	cran = "covid19brazil" 

	version("0.1.0", md5="ad3439514df39b8d04dd16c73d14f59f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
