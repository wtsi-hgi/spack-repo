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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cytoMEM_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cytoMEM/cytoMEM_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="bebc3ea4a8e378788446553b2a7d2e1572c1420d59b44596beb48a9ca5e4083b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
