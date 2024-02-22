# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoval(RPackage):
	"""Procedures for Ecological Assessment of Surface Waters

	Functions for evaluating and visualizing
  ecological assessment procedures for surface waters
  containing physical, chemical and biological assessments
  in the form of value functions.
	"""
	
	cran = "ecoval" 

	version("1.2.9", md5="b6a14e17a3de7fd99cdd49d2a0077d51")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-utility", type=("build", "run"))
	depends_on("r-rivernet", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
