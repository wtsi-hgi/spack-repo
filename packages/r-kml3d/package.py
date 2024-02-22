# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKml3d(RPackage):
	"""K-Means for Joint Longitudinal Data

	An implementation of k-means specifically design
        to cluster joint trajectories (longitudinal data on
        several variable-trajectories).
        Like 'kml', it provides facilities to deal with missing
        value, compute several quality criterion (Calinski and Harabatz,
        Ray and Turie, Davies and Bouldin, BIC,...) and propose a graphical
        interface for choosing the 'best' number of clusters. In addition, the 3D graph
        representing the mean joint-trajectories of each cluster can be exported through
        LaTeX in a 3D dynamic rotating PDF graph.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "kml3d" 

	version("2.4.6.1", md5="26f247d33dafa0a099a0b9c03c7eca06")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-clv", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-longitudinaldata@2.4.2:", type=("build", "run"))
	depends_on("r-kml@2.4.1:", type=("build", "run"))
