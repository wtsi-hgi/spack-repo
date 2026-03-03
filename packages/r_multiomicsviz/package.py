# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiomicsviz(RPackage):
	"""Plot the effect of one omics data on other omics data along the chromosome

	Calculate the spearman correlation between the source omics data and other target omics data, identify the significant correlations and plot the significant correlations on the heat map in which the x-axis and y-axis are ordered by the chromosomal location.
	"""
	
	bioc = "multiOmicsViz" 

	version("1.26.0", commit="6add4409745790d7abfe663f4c8e29a4dff9833e")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
