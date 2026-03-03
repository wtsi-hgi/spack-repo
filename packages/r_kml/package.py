# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKml(RPackage):
	"""K-Means for Longitudinal Data

	An implementation of k-means specifically design
        to cluster longitudinal data. It provides facilities to deal with missing
        value, compute several quality criterion (Calinski and Harabatz,
        Ray and Turie, Davies and Bouldin, BIC, ...) and propose a graphical
        interface for choosing the 'best' number of clusters.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "kml" 

	version("2.4.6.1", md5="a4823c3f7650e59471f7e23e531f1b73")

	depends_on("r-clv", type=("build", "run"))
	depends_on("r-longitudinaldata@2.4:", type=("build", "run"))
