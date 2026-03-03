# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsfa(RPackage):
	"""Slow Feature Analysis

	Slow Feature Analysis (SFA), ported to R based on
    'matlab' implementations of SFA: 'SFA toolkit' 1.0 by Pietro Berkes and 'SFA toolkit'
    2.8 by Wolfgang Konen.
	"""
	
	cran = "rSFA" 

	version("1.5", md5="d579e0531a8d99e270cf71617e0a15b4")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
