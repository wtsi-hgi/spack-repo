# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlexperiment(RPackage):
	"""S4 classes for QTL summary statistics and metadata

	QLTExperiment defines an S4 class for storing and manipulating summary statistics from QTL mapping experiments in one or more states. It is based on the 'SummarizedExperiment' class and contains functions for creating, merging, and subsetting objects. 'QTLExperiment' also stores experiment metadata and has checks in place to ensure that transformations apply correctly.
	"""
	
	homepage = "https://github.com/dunstone-a/QTLExperiment"
	bioc = "QTLExperiment" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/QTLExperiment_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/QTLExperiment/QTLExperiment_1.0.0.tar.gz"]

	version("1.0.0", md5="fe7642e0952c4c68e5417906dfb66fb3")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
