# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiiragi2013(RPackage):
	"""Cell-to-cell expression variability followed by signal reinforcement progressively segregates early mouse lineages

	This package contains the experimental data and a complete executable transcript (vignette) of the statistical analysis presented in the paper "Cell-to-cell expression variability followed by signal reinforcement progressively segregates early mouse lineages" by Y. Ohnishi, W. Huber, A. Tsumura, M. Kang, P. Xenopoulos, K. Kurimoto, A. K. Oles, M. J. Arauzo-Bravo, M. Saitou, A.-K. Hadjantonakis and T. Hiiragi; Nature Cell Biology (2014) 16(1): 27-37. doi: 10.1038/ncb2881."
	"""
	
	bioc = "Hiiragi2013" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Hiiragi2013_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/Hiiragi2013/Hiiragi2013_1.38.0.tar.gz"]

    version("1.44.2", tag="RELEASE_3_21")
	version("1.38.0", sha256="05f5c64944091ca4eee4d498a29b66cccd8168a7afdfb405023d94c2adb0dc13", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Hiiragi2013_1.38.0.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mouse4302-db", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))

