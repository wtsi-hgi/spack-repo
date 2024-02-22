# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarvz(RPackage):
	"""R-Based Visualization Techniques for Task-Based Applications

	Performance analysis workflow that combines the power of the R
    language (and the tidyverse realm) and many auxiliary tools to
    provide a consistent, flexible, extensible, fast, and versatile
    framework for the performance analysis of task-based applications
    that run on top of the StarPU runtime (with its MPI (Message
    Passing Interface) layer for multi-node support).  Its goal is to
    provide a fruitful prototypical environment to conduct performance
    analysis hypothesis-checking for task-based applications that run
    on heterogeneous (multi-GPU, multi-core) multi-node HPC
    (High-performance computing) platforms.
	"""
	
	homepage = "https://github.com/schnorr/starvz"
	cran = "starvz" 

	version("0.7.1", md5="d9dfb23a40c58e2bb379ead91f58f02a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpp@1.0.6:", type=("build", "run"))
	depends_on("r-arrow@3:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("arrow+zlib", type=("build", "link", "run"))
