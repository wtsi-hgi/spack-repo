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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Oscope_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Oscope/Oscope_1.32.0.tar.gz"]

	version("1.32.0", sha256="ae6a2354e1828e29883c48fb949d30bb045b5a74fbe3a3002a000bdc6aa222d2")

	depends_on("r-ebseq", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
