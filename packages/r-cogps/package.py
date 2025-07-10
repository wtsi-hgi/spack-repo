# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCogps(RPackage):
	"""cancer outlier Gene Profile Sets

	Gene Set Enrichment Analysis of P-value based statistics for outlier gene detection in dataset merged from multiple studies
	"""
	
	bioc = "coGPS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/coGPS_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/coGPS/coGPS_1.46.0.tar.gz"]

	version("1.46.0", sha256="a7d77ed813ee2901ad1504856720f0735aabf19e76b95edf99a3da6c911a1752")

	depends_on("r@2.13:", type=("build", "run"))
