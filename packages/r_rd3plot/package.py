# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRd3plot(RPackage):
	"""Interactive Networks, Timelines, Barplots, Galleries with
'D3.js'

	Creates interactive analytic graphs with 'R'. It joins the data analysis power of R and the visualization libraries of JavaScript in one package. The package provides interactive networks, timelines, barplots, image galleries and evolving networks. Graphs are represented as 'D3.js' graphs embedded in a web page ready for its interactive analysis and exploration.
	"""
	
	cran = "rD3plot" 

	version("1.0.68", md5="2feecc3d87f74c8f0233920e5ce58e6c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
