# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasematch(RPackage):
	"""Identify Similar Cases for Qualitative Case Studies

	Allows users to identify similar cases for qualitative case studies using statistical matching methods.
	"""
	
	cran = "caseMatch" 

	version("1.1.0", md5="2037b13ab4d15ed161733c50648cc60d")

