# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgapi(RPackage):
	"""Aid Querying 'nomis' and 'Office for National Statistics Open
Geography' APIs

	Facilitates extraction of geospatial data from the 'Office for National Statistics Open Geography' and 'nomis' Application Programming Interfaces (APIs). Simplifies process of querying 'nomis' datasets <https://www.nomisweb.co.uk/> and extracting desired datasets in dataframe format. Extracts area shapefiles at chosen resolution from 'Office for National Statistics Open Geography' <https://geoportal.statistics.gov.uk/>.
	"""
	
	homepage = "https://defra-data-science-centre-of-excellence.github.io/sgapi/"
	cran = "sgapi" 

	version("1.0.2", md5="afa6ada6d1a99443230917e87e32a68d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
