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

	version("1.22.0", commit="0cda7109ce9a59aadd34a02aaf432dd3dfefd4b9")
	version("1.16.0", commit="80fb82d1cc023e2827c2cde61c98405bc5f6959c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

