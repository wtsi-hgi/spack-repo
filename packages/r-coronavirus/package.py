# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoronavirus(RPackage):
	"""The 2019 Novel Coronavirus COVID-19 (2019-nCoV) Dataset

	Provides a daily summary of the Coronavirus (COVID-19) cases by state/province. Data source: Johns Hopkins University Center for Systems Science and Engineering (JHU CCSE) Coronavirus <https://systems.jhu.edu/research/public-health/ncov/>.
	"""
	
	homepage = "https://github.com/RamiKrispin/coronavirus"
	cran = "coronavirus" 

	version("0.4.1", md5="91e30e9352413473d5fb0762f38737a0")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-devtools@2.2.2:", type=("build", "run"))
