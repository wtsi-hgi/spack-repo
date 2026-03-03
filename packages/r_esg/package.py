# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsg(RPackage):
	"""A Package for Asset Projection

	Presents a "Scenarios" class containing
        general parameters, risk parameters and projection results.
        Risk parameters are gathered together into a ParamsScenarios
        sub-object. The general process for using this package is to
        set all needed parameters in a Scenarios object, use the
        customPathsGeneration method to proceed to the projection, then
        use xxx_PriceDistribution() methods to get asset prices.
	"""
	
	cran = "ESG" 

	version("1.3", md5="44866bd49557f73a002b09a762f62641")

