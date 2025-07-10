# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetactivity(RPackage):
	"""Compute gene set scores from a deep learning framework

	#' NetActivity enables to compute gene set scores from previously trained sparsely-connected autoencoders. The package contains a function to prepare the data (`prepareSummarizedExperiment`) and a function to compute the gene set scores (`computeGeneSetScores`). The package `NetActivityData` contains different pre-trained models to be directly applied to the data. Alternatively, the users might use the package to compute gene set scores using custom models.
	"""
	
	bioc = "NetActivity" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NetActivity_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NetActivity/NetActivity_1.4.0.tar.gz"]

	version("1.4.0", sha256="93e4b6bfe258f29d9d6123dfc0f0aaf332e537211025a4d6c975ee624032324a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-airway", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-netactivitydata", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
