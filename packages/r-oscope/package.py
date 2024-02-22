# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROscope(RPackage):
	"""Oscope - A statistical pipeline for identifying oscillatory genes in unsynchronized single cell RNA-seq

	Oscope is a statistical pipeline developed to identifying and recovering the base cycle profiles of oscillating genes in an unsynchronized single cell RNA-seq experiment. The Oscope pipeline includes three modules: a sine model module to search for candidate oscillator pairs; a K-medoids clustering module to cluster candidate oscillators into groups; and an extended nearest insertion module to recover the base cycle order for each oscillator group.
	"""
	
	bioc = "Oscope" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Oscope_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Oscope/Oscope_1.32.0.tar.gz"]

	version("1.32.0", md5="96a8fc6730b6d493d352d74032c4b3d3")

	depends_on("r-ebseq", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
