# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiclust(RPackage):
	"""BiCluster Algorithms

	The main function biclust() provides several algorithms to
        find biclusters in two-dimensional data: Cheng and Church (2000, ISBN:1-57735-115-0),
        spectral (2003) <doi:10.1101/gr.648603>, plaid model (2005) <doi:10.1016/j.csda.2004.02.003>, xmotifs (2003) <doi:10.1142/9789812776303_0008> and bimax (2006) <doi:10.1093/bioinformatics/btl060>. In addition, the
        package provides methods for data preprocessing (normalization
        and discretisation), visualisation, and validation of bicluster
        solutions.
	"""
	
	cran = "biclust" 

	version("2.0.3.1", md5="09df04f1531cebcb9c7654ed2e4bfe65")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-additivitytests", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
