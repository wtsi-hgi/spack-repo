# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSapevom(RPackage):
	"""Group Ordinal Method for Multiple Criteria Decision-Making

	Implementation of SAPEVO-M, a Group Ordinal Method for Multiple Criteria Decision-Making (MCDM). SAPEVO-M is an acronym for Simple Aggregation of Preferences Expressed by Ordinal Vectors Group Decision Making. This method provides alternatives ranking given decision makers' preferences: criteria preferences and alternatives preferences for each criterion.This method is described in Gomes et al. (2020) <doi: 10.1590/0101-7438.2020.040.00226524 >.
	"""
	
	cran = "sapevom" 

	version("0.2.0", md5="1f09e804018b2746f9c7ec305bf0fce5")

