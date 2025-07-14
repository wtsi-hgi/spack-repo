# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsbenchmark(RPackage):
	"""Gene Set Benchmark

	Benchmarks for Machine Learning Analysis of the Gene Sets. The package contains a list of pathways and gene expression data sets used in "Identifying Tightly Regulated and Variably Expressed Networks by Differential Rank Conservation (DIRAC)" (2010) by Eddy et al.
	"""
	
	bioc = "GSBenchMark"

	version("1.28.0", commit="38e89d87030bcbfa3d788c242941e5d15a3e0cad")
	version("1.22.0", commit="abb8bad4565ef4cb38f52555f70a6ffd8d4bf4e7")

	depends_on("r@2.13.1:", type=("build", "run"))

