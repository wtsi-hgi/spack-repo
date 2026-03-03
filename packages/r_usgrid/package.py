# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsgrid(RPackage):
	"""The Demand and Supply for Electricity in the US

	Provides a set of regular time-series datasets, describing the US electricity grid. That includes the total demand and supply, and as well as the demand by energy source (coal, solar, wind, etc.). Source: US Energy Information Administration (Dec 2019) <https://www.eia.gov/>.
	"""
	
	homepage = "https://github.com/RamiKrispin/USgrid"
	cran = "USgrid" 

	version("0.1.2", md5="bf3bb8a2f6e605bc49839a8156a22ac5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-tsibble@0.8.5:", type=("build", "run"))
