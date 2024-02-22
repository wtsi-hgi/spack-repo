# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantileda(RPackage):
	"""Quantile Classifier

	Code for centroid, median and quantile classifiers.
	"""
	
	cran = "quantileDA" 

	version("1.1", md5="700adfa579c81b08845742fa0364c98a")

