# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmqcm(RPackage):
	"""An Algorithm for Gene Co-Expression Analysis

	Implementation based on Zhang, Jie & Huang, Kun (2014) <doi:10.4137/CIN.S14021> Normalized ImQCM: An Algorithm for Detecting Weak Quasi-Cliques in Weighted Graph with Applications in Gene Co-Expression Module Discovery in Cancers. Cancer informatics, 13, CIN-S14021.
	"""
	
	homepage = "https://github.com/huangzhii/lmQCM/"
	cran = "lmQCM" 

	version("0.2.4", md5="ebe999550fa59cdc15877b9e5066ae5d")

	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
