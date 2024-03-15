# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenchmarkfdrdata2019(RPackage):
	"""Data and Benchmarking Results from Korthauer and Kimes et al. (2019)

	Benchmarking results for experimental and simulated data sets used in Korthauer and Kimes et al. (2019) to compare methods for controlling the false discovery rate.
	"""
	
	bioc = "benchmarkfdrData2019" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/benchmarkfdrData2019_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/benchmarkfdrData2019/benchmarkfdrData2019_1.16.0.tar.gz"]

	version("1.16.0", md5="50ce7eb4100da1909ddd6c71c31e7e0c", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/benchmarkfdrData2019_1.16.0.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment