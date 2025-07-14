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

	version("1.20.0", commit="a541d3e1f21cd14a82631ac81c9036c4a4d6607a")
	version("1.14.0", commit="cbe77193c726f42d19a23cb1d14f67b4fdb0a479")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
