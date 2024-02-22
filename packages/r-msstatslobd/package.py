# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatslobd(RPackage):
	"""Assay characterization: estimation of limit of blanc(LoB) and limit of detection(LOD)

	The MSstatsLOBD package allows calculation and visualization of limit of blac (LOB) and limit of detection (LOD). We define the LOB as the highest apparent concentration of a peptide expected when replicates of a blank sample containing no peptides are measured. The LOD is defined as the measured concentration value for which the probability of falsely claiming the absence of a peptide in the sample is 0.05, given a probability 0.05 of falsely claiming its presence. These functionalities were previously a part of the MSstats package. The methodology is described in Galitzine (2018) <doi:10.1074/mcp.RA117.000322>.
	"""
	
	bioc = "MSstatsLOBD" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MSstatsLOBD_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MSstatsLOBD/MSstatsLOBD_1.10.0.tar.gz"]

	version("1.10.0", md5="1d67c5813cb057b72100d71487c26f64")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
