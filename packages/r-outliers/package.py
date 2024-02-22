# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutliers(RPackage):
	"""Tests for Outliers

	A collection of some tests commonly used for identifying
        outliers.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "outliers" 

	version("0.15", md5="be743c547e809a684e2831e82e88206b")

	depends_on("r@2:", type=("build", "run"))
