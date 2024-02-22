# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLipidmapsr(RPackage):
	"""Lipid Maps Rest Service

	Lipid Maps Rest service. Researchers can access the Lipid Maps Rest
  service programmatically and conveniently integrate it into the current workflow
  or packages.
	"""
	
	cran = "lipidmapsR" 

	version("1.0.4", md5="5607070b4bd8a69f60804504d3952eff")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-rjsonio@1.3.0:", type=("build", "run"))
