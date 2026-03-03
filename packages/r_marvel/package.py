# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarvel(RPackage):
	"""Revealing Splicing Dynamics at Single-Cell Resolution

	Alternative splicing represents an additional and underappreciated layer of complexity underlying gene expression profiles. Nevertheless, there remains hitherto a paucity of software to investigate splicing dynamics at single-cell resolution. 'MARVEL' enables splicing analysis of single-cell RNA-sequencing data generated from plate- and droplet-based library preparation methods.
	"""
	
	cran = "MARVEL" 

	version("1.4.0", md5="c0fbef322e4c0d72c0a515b88403e479")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-matrix@1.3.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
