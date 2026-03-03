# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdgecorr(RPackage):
	"""Spatial Edge Correction

	Facilitates basic spatial edge correction to point pattern data.
	"""
	
	cran = "edgeCorr" 

	version("1.0", md5="244286527300c334cf56976baad04dfb")

