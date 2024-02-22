# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaribou(RPackage):
	"""Estimation of Caribou Abundance Based on Radio Telemetry Data

	Estimation of population size of migratory caribou herds based on large scale 
             aggregations monitored by radio telemetry. It implements the methodology found 
             in the article by Rivest et al. (1998) about caribou abundance estimation. It 
             also includes a function based on the Lincoln-Petersen Index as applied to 
             radio telemetry data by White and Garrott (1990).
	"""
	
	cran = "caribou" 

	version("1.1-1", md5="8e5ab7e4549b1f866c9232e73a8260e8")

