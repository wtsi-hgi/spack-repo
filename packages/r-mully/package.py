# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMully(RPackage):
	"""Create, Modify and Visualize Multi-Layered Networks

	Allows the user to create graphs with multiple layers. The user can also modify the layers, the nodes, and the edges. The graph can also be visualized.
    Zaynab Hammoud and Frank Kramer (2018) <doi:10.3390/genes9110519>.
    More about multilayered graphs and their usage can be found in our review paper:
    Zaynab Hammoud and Frank Kramer (2020) <doi:10.1186/s41044-020-00046-0>.
	"""
	
	homepage = "https://github.com/frankkramer-lab/mully"
	cran = "mully" 

	version("2.1.38", md5="9ce70f56da708186f3dc1156f93dcba5")

	depends_on("r-igraph@1.3.5.9097:", type=("build", "run"))
	depends_on("r-rgl@1:", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
