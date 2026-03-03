# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhpcbenchmark(RPackage):
	"""Benchmarks for High-Performance Computing Environments

	Microbenchmarks for determining the run time
  performance of aspects of the R programming environment and packages
  relevant to high-performance computation.  The benchmarks are divided into
  three categories: dense matrix linear algebra kernels, sparse matrix linear
  algebra kernels, and machine learning functionality.
	"""
	
	cran = "RHPCBenchmark" 

	version("0.1.0", md5="e52c17cbb3c69f590b13555a5a3786da")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
