# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoma(RPackage):
	"""Multi Omic Master Regulator Analysis

	This package implements the inference of candidate master regulator proteins from multi-omics' data (MOMA) algorithm, as well as ancillary analysis and visualization functions.
	"""
	
	bioc = "MOMA"

	version("1.20.0", commit="ee54dc10294b1aae33efad26646a64184b3bf611")
	version("1.14.0", commit="44545822dccfc0ddf058156b22126fc193052214")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mkmisc", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
