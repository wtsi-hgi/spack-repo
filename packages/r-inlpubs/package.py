# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInlpubs(RPackage):
	"""USGS INL Project Office Publications

	Contains bibliographic information for the U.S. Geological Survey
    (USGS) Idaho National Laboratory (INL) Project Office.
	"""
	
	homepage = "https://rconnect.usgs.gov/INLPO/inlpubs-main/"
	cran = "inlpubs" 

	version("1.0.6", md5="c09ae0059b82761efed559c3630d7dd0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
