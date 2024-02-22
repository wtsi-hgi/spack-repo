# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19italy(RPackage):
	"""The 2019 Novel Coronavirus COVID-19 (2019-nCoV) Italy Dataset

	Provides a daily summary of the Coronavirus (COVID-19) cases in Italy by country, region and province level. Data source: Presidenza del Consiglio dei Ministri - Dipartimento della Protezione Civile <https://www.protezionecivile.it/>.
	"""
	
	homepage = "https://github.com/RamiKrispin/covid19italy"
	cran = "covid19italy" 

	version("0.3.1", md5="435927862afa918d1ea392e581c1f2d8")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
