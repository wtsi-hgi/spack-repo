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

	version("2.0.1", commit="6cbea032523522aca2a5de258b57cccaccb55bcd")
	version("1.0.0", commit="eb387bfec58bc3aa7302071d0b5a28ba7d81a4ec")

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
