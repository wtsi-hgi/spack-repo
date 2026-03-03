# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19srilanka(RPackage):
	"""The 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data in Sri
Lanka

	Provides a daily counts of the Coronavirus (COVID19) cases by districts and country. Data source: Epidemiological Unit, Ministry of Health, Sri Lanka <https://www.epid.gov.lk/web/>.
	"""
	
	cran = "covid19srilanka" 

	version("1.1.0", md5="6d17b8290e6b7642aca151cc18b73b8c")

	depends_on("r@2.10:", type=("build", "run"))
