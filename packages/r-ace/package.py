# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAce(RPackage):
	"""Absolute Copy Number Estimation from Low-coverage Whole Genome Sequencing

	Uses segmented copy number data to estimate tumor cell percentage and produce copy number plots displaying absolute copy numbers.
	"""
	
	homepage = "https://github.com/tgac-vumc/ACE"
	bioc = "ACE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ACE_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ACE/ACE_1.20.0.tar.gz"]

	version("1.20.0", md5="dd177150c01a5547ca8edabf82ef85d6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-qdnaseq", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
