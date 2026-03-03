# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsgas(RPackage):
	"""The Demand for Natural Gas in the US

	Provides an overview of the demand for natural gas in the US by state and country level. Data source: US Energy Information Administration <https://www.eia.gov/>.
	"""
	
	homepage = "https://github.com/RamiKrispin/USgas"
	cran = "USgas" 

	version("0.1.2", md5="8a596fe1683d59be338f8fce53064502")

	depends_on("r@2.10:", type=("build", "run"))
