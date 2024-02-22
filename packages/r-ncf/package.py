# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcf(RPackage):
	"""Spatial Covariance Functions

	Spatial (cross-)covariance and related geostatistical tools: the
        nonparametric (cross-)covariance function , the spline correlogram, the
        nonparametric phase coherence function, local indicators of spatial 
        association (LISA), (Mantel) correlogram, (Partial) Mantel test.
	"""
	
	homepage = "https://ento.psu.edu/directory/onb1"
	cran = "ncf" 

	version("1.3-2", md5="430497c09c6aa32051b86f12b0d27724")

	depends_on("r@2.8:", type=("build", "run"))
