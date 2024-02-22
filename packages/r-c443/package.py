# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RC443(RPackage):
	"""See a Forest for the Trees

	Get insight into a forest of classification trees, by calculating similarities between the trees, and subsequently clustering them. Each cluster is represented by it's most central cluster member. The package implements the methodology described in Sies & Van Mechelen (2020) <doi:10.1007/s00357-019-09350-4>.
	"""
	
	homepage = "https://github.com/KULeuven-PPW-OKPIV/C443"
	cran = "C443" 

	version("3.4.0", md5="b5ff39d3ef2fe33c652d9ba8ce45749d", url="https://cran.r-project.org/src/contrib/C443_3.4.0.tar.gz")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
