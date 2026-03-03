# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReca(RPackage):
	"""Relevant Component Analysis for Supervised Distance Metric
Learning

	Relevant Component Analysis (RCA) tries to find a linear
    transformation of the feature space such that the effect of irrelevant
    variability is reduced in the transformed space.
	"""
	
	homepage = "https://nanx.me/RECA/"
	cran = "RECA" 

	version("1.7", md5="63c9a66621d9a94ac7b45fec575c4fe7")

