# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApollonius(RPackage):
	"""2D Apollonius Graphs

	Computation of the Apollonius diagram of given 2D points and
	its dual the Apollonius graph, also known as the additively weighted
	Voronoï diagram, and which is a generalization of the classical Voronoï 
	diagram. For references, see the bibliography in the CGAL documentation 
	at <https://doc.cgal.org/latest/Apollonius_graph_2/citelist.html>.
	"""
	
	homepage = "https://github.com/stla/Apollonius"
	cran = "Apollonius"

	version("1.0.1", md5="3b0a331134639251500963c99b67d653")

	depends_on("r-abind", type=("build", "run"))
	depends_on("r-colorsgen", type=("build", "run"))
	depends_on("r-gyro@1.3:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppcgal", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
	depends_on("mpfr", type=("build", "link", "run"))
