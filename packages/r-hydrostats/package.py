# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrostats(RPackage):
	"""Hydrologic Indices for Daily Time Series Data

	Calculates a suite of hydrologic indices for daily time series data that are widely used in hydrology and stream ecology.
	"""
	
	homepage = "https://github.com/nickbond/hydrostats"
	cran = "hydrostats" 

	version("0.2.9", md5="e5af04067cd8a626de9735891ba242b1")

