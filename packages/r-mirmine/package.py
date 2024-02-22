# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirmine(RPackage):
	"""Data package with miRNA-seq datasets from miRmine database as RangedSummarizedExperiment

	miRmine database is a collection of expression profiles from different publicly available miRNA-seq datasets, Panwar et al (2017) miRmine: A Database of Human miRNA Expression, prepared with this data package as RangedSummarizedExperiment.
	"""
	
	bioc = "miRmine" 

	version("1.24.0", commit="868b57a415c3c1da22c114df2b48f41365c28426")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
