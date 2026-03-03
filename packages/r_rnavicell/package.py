# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnavicell(RPackage):
	"""Visualization of High-Throughput Data on Large-Scale Biological
Networks

	Provides a set of functions to access a data visualization web service. For more information and a tutorial on how to use it, see https://navicell.curie.fr/pages/nav_web_service.html and https://github.com/sysbio-curie/RNaviCell. 
	"""
	
	cran = "RNaviCell" 

	version("0.2", md5="64b96078aae343b60a00f33be0f86745")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
