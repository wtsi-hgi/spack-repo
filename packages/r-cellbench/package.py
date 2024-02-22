# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellbench(RPackage):
	"""Construct Benchmarks for Single Cell Analysis Methods

	This package contains infrastructure for benchmarking analysis methods and access to single cell mixture benchmarking data. It provides a framework for organising analysis methods and testing combinations of methods in a pipeline without explicitly laying out each combination. It also provides utilities for sampling and filtering SingleCellExperiment objects, constructing lists of functions with varying parameters, and multithreaded evaluation of analysis methods.
	"""
	
	homepage = "https://github.com/shians/cellbench"
	bioc = "CellBench" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CellBench_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CellBench/CellBench_1.18.0.tar.gz"]

	version("1.18.0", md5="21b854517881e111491fd4b6dba0857c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
