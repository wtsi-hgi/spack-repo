# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFst4pg(RPackage):
	"""Genetic Distance Segmentation for Population Genetics

	Provides efficient methods to compute local and genome wide
    genetic distances (corresponding to the so called Hudson Fst
    parameters) through moment method, perform chromosome segmentation
    into homogeneous Fst genomic regions, and selection sweep detection
    for multi-population comparison. When multiple profile segmentation is
    required, the procedure can be parallelized using the future package.
	"""
	
	cran = "fst4pg" 

	version("1.0.0", md5="ee6f08f4cfc9d4a88f50b786d7bf284e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fpopw", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
