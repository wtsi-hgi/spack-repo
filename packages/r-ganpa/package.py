# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGanpa(RPackage):
	"""Gene Association Network-Based Pathway Analysis (GANPA)

	A network-based gene weighting algorithm for pathway enrichment analysis, using either RNA-seq or microarray data. Zhaoyuan Fang, Weidong Tian and Hongbin Ji (2012) <doi:10.1038/cr.2011.149>.
	"""
	
	cran = "GANPA" 

	version("1.1", md5="6bcc285a9e5f9564610b84be3fc57725")

	depends_on("r-ganpadata", type=("build", "run"))
