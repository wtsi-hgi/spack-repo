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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GSBenchMark_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/GSBenchMark/GSBenchMark_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="eb89db2991aa2c7f9945ea5e0f19325fe97060220e74c09dbb2082990cbb8c0d")

	depends_on("r@2.13.1:", type=("build", "run"))

