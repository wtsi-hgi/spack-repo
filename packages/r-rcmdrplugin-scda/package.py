# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginScda(RPackage):
	"""Rcmdr Plugin for Designing and Analyzing Single-Case Experiments

	Provides a GUI for the SCVA, SCRT and SCMA packages as described in Bulte and Onghena (2013) <doi:10.22237/jmasm/1383280020>. The package is written as an Rcmdr plugin.
	"""
	
	cran = "RcmdrPlugin.SCDA" 

	version("1.2.0", md5="bbc79d9958b3ad6d299690c762a5c534")

	depends_on("r-scva", type=("build", "run"))
	depends_on("r-scrt", type=("build", "run"))
	depends_on("r-scma", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
