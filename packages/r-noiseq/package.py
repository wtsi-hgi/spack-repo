# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoiseq(RPackage):
	"""Exploratory analysis and differential expression for RNA-seq data

	Analysis of RNA-seq expression data or other similar kind of data. Exploratory plots to evualuate saturation, count distribution, expression per chromosome, type of detected features, features length, etc. Differential expression between two experimental conditions with no parametric assumptions.
	"""
	
	bioc = "NOISeq"

	version("2.52.0", commit="ea46e92b8fa909376c638c96caefe520d8f25ee2")
	version("2.46.0", commit="45f591704d3e4ced39a04c69b9b6a8f620d3cc29")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase@2.13.11:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
