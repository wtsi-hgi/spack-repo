# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlluvial(RPackage):
	"""Alluvial Diagrams

	Creating alluvial diagrams (also known as parallel sets plots) for multivariate
  and time series-like data.
	"""
	
	homepage = "https://github.com/mbojan/alluvial"
	cran = "alluvial" 

	version("0.1-2", md5="7666ad9699dd92f470499b62a70c2c8a")

