# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepdat(RPackage):
	"""Peptide microarray data package

	Provides sample files and data for the vignettes of pepStat and Pviz as well as peptide collections for HIV and SIV.
	"""
	
	bioc = "pepDat" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/pepDat_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/pepDat/pepDat_1.22.0.tar.gz"]

	version("1.22.0", md5="4ce373369604b54b15e5992ebe9355b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

	# experiment