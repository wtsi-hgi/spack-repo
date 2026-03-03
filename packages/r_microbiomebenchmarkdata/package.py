# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomebenchmarkdata(RPackage):
	"""Datasets for benchmarking in microbiome research

	The MicrobiomeBenchmarkData package provides functionality to access microbiome datasets suitable for benchmarking. These datasets have some biological truth, which allows to have expected results for comparison. The datasets come from various published sources and are provided as TreeSummarizedExperiment objects. Currently, only datasets suitable for benchmarking differential abundance methods are available.
	"""
	
	homepage = "https://github.com/waldronlab/MicrobiomeBenchmarkData"
	bioc = "MicrobiomeBenchmarkData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MicrobiomeBenchmarkData_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MicrobiomeBenchmarkData/MicrobiomeBenchmarkData_1.4.0.tar.gz"]

	version("1.4.0", md5="c6c791669de95bf2dc108798770ea5be")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-treesummarizedexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))

