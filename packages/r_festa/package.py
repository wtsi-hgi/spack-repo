# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFesta(RPackage):
	"""Fishing Effort Standardisation

	Original idea was presented in the reference paper. Varghese et al. (2020, 74(1):35-42) "Bayesian State-space Implementation of Schaefer Production Model for Assessment of Stock Status for Multi-gear Fishery". Marine fisheries governance and management practices are very essential to ensure the sustainability of the marine resources. A widely accepted resource management strategy towards this is to derive sustainable fish harvest levels based on the status of marine fish stock. Various fish stock assessment models that describe the biomass dynamics using time series data on fish catch and fishing effort are generally used for this purpose. In the scenario of complex multi-species marine fishery in which different species are caught by a number of fishing gears and each gear harvests a number of species make it difficult to obtain the fishing effort corresponding to each fish species. Since the capacity of the gears varies, the effort made to catch a resource cannot be considered as the sum of efforts expended by different fishing gears. This necessitates standardisation of fishing effort in unit base.
	"""
	
	cran = "FESta" 

	version("1.0.0", md5="dfcce2ceea616abc262df8299fc54b0a")

