# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmcsr(RPackage):
	"""Mismatch Tolerant Maximum Common Substructure Searching

	The fmcsR package introduces an efficient maximum common substructure (MCS) algorithms combined with a novel matching strategy that allows for atom and/or bond mismatches in the substructures shared among two small molecules. The resulting flexible MCSs (FMCSs) are often larger than strict MCSs, resulting in the identification of more common features in their source structures, as well as a higher sensitivity in finding compounds with weak structural similarities. The fmcsR package provides several utilities to use the FMCS algorithm for pairwise compound comparisons, structure similarity searching and clustering.
	"""
	
	homepage = "https://github.com/girke-lab/fmcsR"
	bioc = "fmcsR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fmcsR_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fmcsR/fmcsR_1.44.0.tar.gz"]

	version("1.44.0", md5="21a6242a61cba8dd537bf846af3260c3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
