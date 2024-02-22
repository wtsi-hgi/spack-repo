# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsco08conversions(RPackage):
	"""Converts ISCO-08 to Job Prestige Scores, ISCO-88 and Job Name

	Implementation of functions to assign corresponding common job prestige scores (SIOPS, ISEI), the official job or group title and the ISCO-88 code to given ISCO-08 codes. ISCO-08 is the latest version of the International Standard Classification of Occupations which is used to organise information on labour and jobs. 
	"""
	
	cran = "ISCO08ConveRsions" 

	version("0.2.0", md5="dd6683b65f791bb05759032c846035a8")

