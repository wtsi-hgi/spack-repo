# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigqc(RPackage):
	"""Quality Control Metrics for Gene Signatures

	Provides gene signature quality control metrics in publication ready plots. Namely, enables the visualization of properties such as expression, variability, correlation, and comparison of methods of standardisation and scoring metrics.
	"""
	
	cran = "sigQC" 

	version("0.1.23", md5="334aaa384c214ab66308e428eb5d729a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-gridgraphics", type=("build", "run"))
	depends_on("r-biclust", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
