# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhldata(RPackage):
	"""Scores for Every Season Since the Founding of the NHL in 1917

	Each dataset contains scores for every game during a specific season of the NHL.
	"""
	
	cran = "NHLData" 

	version("1.0.0", md5="49db1c366014dbd29d99a7a43787a89c")

	depends_on("r@2.10:", type=("build", "run"))
