# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPegas(RPackage):
	"""Population and Evolutionary Genetics Analysis System.

	Functions for reading, writing, plotting, analysing, and manipulating
	allelic and haplotypic data, including from VCF files, and for the analysis
	of population nucleotide sequences and micro-satellites including
	coalescent analyses, linkage disequilibrium, population structure (Fst,
	Amova) and equilibrium (HWE), haplotype networks, minimum spanning tree and
	network, and median-joining networks."""

	cran = "pegas"

	maintainers("dorton21")

	license("GPL-2.0-or-later")

	version("1.3", md5="95288acee475f26e94077b9962cc9848")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ape@5.3.11:", type=("build", "run"))
