# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBisep(RPackage):
	"""Toolkit to Identify Candidate Synthetic Lethality

	Enables the user to infer potential synthetic lethal relationships
    by analysing relationships between bimodally distributed gene pairs in big
    gene expression datasets.  Enables the user to visualise these candidate
    synthetic lethal relationships.
	"""
	
	cran = "BiSEp" 

	version("2.2", md5="227e7f3a87c8a2dea7f6cd5bf64f76e7")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-mclust@4.2:", type=("build", "run"))
	depends_on("r-gosemsim@2.0.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
