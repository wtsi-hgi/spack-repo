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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/pepDat_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/pepDat/pepDat_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="03bfe8a1b944e4821fbacb8fb0a93755e008242cd909a229d8ae3fce5da7454f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

