# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpqn(RPackage):
	"""Spatial quantile normalization

	The spqn package implements spatial quantile normalization (SpQN). This method was developed to remove a mean-correlation relationship in correlation matrices built from gene expression data. It can serve as pre-processing step prior to a co-expression analysis.
	"""
	
	homepage = "https://github.com/hansenlab/spqn"
	bioc = "spqn" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/spqn_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/spqn/spqn_1.14.0.tar.gz"]

	version("1.14.0", sha256="0b09efbc6cf24160cd6d661a13751f3b0e545180d5260a75dbce762a2ff0d01e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
