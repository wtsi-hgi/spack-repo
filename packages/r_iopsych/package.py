# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIopsych(RPackage):
	"""Methods for Industrial/Organizational Psychology

	Collection of functions for IO Psychologists.
	"""
	
	cran = "iopsych" 

	version("0.90.1", md5="e76dc0b476fd4c7a696c190f86587bb8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mvtnorm@1:", type=("build", "run"))
	depends_on("r-mco@1:", type=("build", "run"))
