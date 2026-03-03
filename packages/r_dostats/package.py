# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDostats(RPackage):
	"""Compute Statistics Helper Functions

	A small package containing helper utilities for creating functions
    for computing statistics.
	"""
	
	homepage = "https://github.com/halpo/dostats"
	cran = "dostats" 

	version("1.3.3", md5="8e40286ca2bb2fe36a67cf7b7ae3b27b")

	depends_on("r@2.12:", type=("build", "run"))
