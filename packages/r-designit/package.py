# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesignit(RPackage):
	"""Blocking and Randomization for Experimental Design

	
    Intelligently assign samples to batches in order to reduce batch effects.
    Batch effects can have a significant impact on data analysis, especially
    when the assignment of samples to batches coincides with the contrast
    groups being studied. By defining a batch container and a scoring function
    that reflects the contrasts, this package allows users to assign samples in
    a way that minimizes the potential impact of batch effects on the
    comparison of interest. Among other functionality, we provide an
    implementation for OSAT score by Yan et al. (2012,
    <doi:10.1186/1471-2164-13-689>).
	"""
	
	homepage = "https://bedapub.github.io/designit/"
	cran = "designit" 

	version("0.5.0", md5="535c66b339a0a0ecd865d8f75b2a7055")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
