# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScthi(RPackage):
	"""Indentification of significantly activated ligand-receptor interactions across clusters of cells from single-cell RNA sequencing data

	scTHI is an R package to identify active pairs of ligand-receptors from single cells in order to study,among others, tumor-host interactions. scTHI contains a set of signatures to classify cells from the tumor microenvironment.
	"""
	
	bioc = "scTHI" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scTHI_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scTHI/scTHI_1.14.0.tar.gz"]

	version("1.14.0", sha256="1db7bf0ba9fc9a32bce57156aa0ce44500d3b8ed1ec133c0a06099aecd3a7ac6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
