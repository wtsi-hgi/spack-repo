# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMta(RPackage):
	"""Multiscalar Territorial Analysis

	Build multiscalar territorial analysis based on various contexts.
	"""
	
	homepage = "https://github.com/riatelab/MTA/"
	cran = "MTA" 

	version("0.6.0", md5="3228f4acb0fdee3ea846059a2e04b81c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
