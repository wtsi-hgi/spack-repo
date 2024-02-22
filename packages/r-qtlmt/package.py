# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlmt(RPackage):
	"""Tools for Mapping Multiple Complex Traits

	Provides tools for joint analysis of multiple traits in a backcross (BC) or recombinant inbred lines (RIL) population. It can be used to select an optimal subset of traits for multiple-trait mapping, analyze multiple traits via the SURE model, which can associate different QTL with different traits, and perform multiple-trait composite multiple-interval mapping.
	"""
	
	cran = "qtlmt" 

	version("0.1-6", md5="187a11f2c8090d6190a289dff1631e1a")

	depends_on("r@2.10:", type=("build", "run"))
