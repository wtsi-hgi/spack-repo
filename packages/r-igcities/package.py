# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgcities(RPackage):
	"""Simulate Impact of Different Urban Policies Through a General
Equilibrium Model

	Develops a General Equilibrium (GE) Model, which estimates key variables such as wages, the number of residents and workers, the prices of the floor space, and its distribution between commercial and residential use, as in Ahlfeldt et al., (2015) <https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA10876>. By doing so, the model allows understanding the economic influence of different urban policies.
	"""
	
	cran = "IGCities" 

	version("0.2.0", md5="d150fe17d037430d52b794f6055fd544")

