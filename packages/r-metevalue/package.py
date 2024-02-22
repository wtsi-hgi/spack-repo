# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetevalue(RPackage):
	"""E-Value in the Omics Data Association Studies

	In the omics data association studies, it is common to conduct the p-value corrections to control the false significance. Beyond the P-value corrections, E-value is recently studied to facilitate multiple testing correction based on V. Vovk and R. Wang (2021) <doi:10.1214/20-AOS2020>. This package provides E-value calculation for DNA methylation data and RNA-seq data. Currently, five data formats are supported: DNA methylation levels using DMR detection tools (BiSeq, DMRfinder, MethylKit, Metilene and other DNA methylation tools) and RNA-seq data. The relevant references are listed below: Katja Hebestreit and Hans-Ulrich Klein (2022) <doi:10.18129/B9.bioc.BiSeq>; Altuna Akalin et.al (2012) <doi:10.18129/B9.bioc.methylKit>.
	"""
	
	cran = "metevalue" 

	version("0.2.4", md5="5df0a8751e473cea80b84ede3810ddb5")

	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
