# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcosim(RPackage):
	"""Toolbox for Aquatic Ecosystem Modeling

	Classes and methods for implementing aquatic ecosystem models,
  for running these models, and for visualizing their results.
	"""
	
	cran = "ecosim" 

	version("1.3-4", md5="bd3c815628ef8e9ec25b57434071e9fd")

	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-stoichcalc", type=("build", "run"))
