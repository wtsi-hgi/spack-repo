# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVelociraptr(RPackage):
	"""Fossil Analysis

	Functions for downloading, reshaping, culling, cleaning, and analyzing fossil data from the Paleobiology Database <https://paleobiodb.org>.
	"""
	
	cran = "velociraptr" 

	version("1.1.0", md5="b3807f49aecf9ca5e746a312a9e46df4")

	depends_on("r-sf", type=("build", "run"))
