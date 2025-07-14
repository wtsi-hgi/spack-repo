# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmappr2data(RPackage):
	"""Sample Data for MMAPPR2

	Contains data for illustration purposes in the MMAPPR2 package, namely simulated BAM files containing RNA-Seq data for a mutation in the slc24a5 gene, taken from the GRCz11 genome. Also contains reference sequence and annotation files for the region.
	"""
	
	homepage = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3613585/"
	bioc = "MMAPPR2data"

	version("1.16.0", commit="b6e09506943bb41724f1c927efba92d11b20df31")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))

