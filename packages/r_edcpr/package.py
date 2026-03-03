# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdcpr(RPackage):
	"""Ecological Data Collection and Processing Package

	This is the course package for the exercise portion of the "Ecological Data Collection and Processing" course.
	"""
	
	cran = "edcpR" 

	version("1.0.1", md5="74ede79cf522e3b297ebc9dbe1ceb815")

	depends_on("r@2.10:", type=("build", "run"))
