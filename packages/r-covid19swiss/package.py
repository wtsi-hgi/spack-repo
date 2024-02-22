# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19swiss(RPackage):
	"""COVID-19 Cases in Switzerland and Principality of Liechtenstein

	Provides a daily summary of the Coronavirus (COVID-19) cases in Switzerland cantons and Principality of Liechtenstein. Data source: Specialist Unit for Open Government Data Canton of Zurich <https://www.zh.ch/de/politik-staat/opendata.html>.
	"""
	
	homepage = "https://github.com/Covid19R/covid19swiss"
	cran = "covid19swiss" 

	version("0.1.0", md5="05c30698b920581ce9c94af788cc06d0")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
