# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNice(RPackage):
	"""Get or Set UNIX Niceness

	Get or set UNIX priority (niceness) of running R process.
	"""
	
	cran = "nice" 

	version("0.4-2", md5="e4c1a883e841d123ea18baf54ab779b9")

	depends_on("r@2.10:", type=("build", "run"))
