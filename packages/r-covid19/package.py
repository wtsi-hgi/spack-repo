# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19(RPackage):
	"""R Interface to COVID-19 Data Hub

	Provides a daily summary of COVID-19 cases, deaths, recovered, tests,
  vaccinations, and hospitalizations for 230+ countries, 760+ regions, 
  and 12000+ administrative divisions of lower level. 
  Includes policy measures, mobility data, and geospatial identifiers.
  Data source: COVID-19 Data Hub <https://covid19datahub.io>.
	"""
	
	homepage = "https://covid19datahub.io"
	cran = "COVID19" 

	version("3.0.3", md5="ad1f2171c0803aa57ed7293bcca49984", url="https://cran.r-project.org/src/contrib/COVID19_3.0.3.tar.gz")

	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
