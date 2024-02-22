# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSankey(RPackage):
	"""Illustrate the Flow of Information or Material

	Plots that illustrate the flow of information or material.
	"""
	
	homepage = "https://github.com/gaborcsardi/sankey#readme"
	cran = "sankey" 

	version("1.0.2", md5="98e63b340cebbb3d5b9dae1078512bb3")

	depends_on("r-simplegraph", type=("build", "run"))
