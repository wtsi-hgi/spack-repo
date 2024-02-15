# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeriation(RPackage):
	"""Infrastructure for Ordering Objects Using Seriation

	Infrastructure for ordering objects with an implementation of several
    seriation/sequencing/ordination techniques to reorder matrices, dissimilarity
    matrices, and dendrograms. Also provides (optimally) reordered heatmaps,
    color images and clustering visualizations like dissimilarity plots, and
    visual assessment of cluster tendency plots (VAT and iVAT). Hahsler et al (2008) <doi:10.18637/jss.v025.i03>.
	"""
	
	homepage = "https://github.com/mhahsler/seriation"
	cran = "seriation" 

	version("1.5.4", md5="e44c7b7bfe1340609df38646cbdccf3c")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ca", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gclus", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-qap", type=("build", "run"))
	depends_on("r-registry", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))

