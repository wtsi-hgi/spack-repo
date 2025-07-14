# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytomem(RPackage):
	"""Marker Enrichment Modeling (MEM)

	MEM, Marker Enrichment Modeling, automatically generates and displays quantitative labels for cell populations that have been identified from single-cell data. The input for MEM is a dataset that has pre-clustered or pre-gated populations with cells in rows and features in columns. Labels convey a list of measured features and the features' levels of relative enrichment on each population. MEM can be applied to a wide variety of data types and can compare between MEM labels from flow cytometry, mass cytometry, single cell RNA-seq, and spectral flow cytometry using RMSD.
	"""
	
	homepage = "https://github.com/cytolab/cytoMEM"
	bioc = "cytoMEM"

	version("1.12.0", commit="e4cb9522fe64dbbe62e2c8f088962efcfa4ef9a5")
	version("1.6.0", commit="0556dc38733c9e5813485ad84a7c36baba6d9ccc")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
