# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootstrapqtl(RPackage):
	"""Bootstrap cis-QTL Method that Corrects for the Winner's Curse

	Identifies genome-related molecular traits with significant 
  evidence of genetic regulation and performs a bootstrap procedure to 
  correct estimated effect sizes for over-estimation present in cis-QTL
  mapping studies (The "Winner's Curse"), described in Huang QQ *et al.* 
  2018 <doi: 10.1093/nar/gky780>. 
	"""
	
	cran = "BootstrapQTL" 

	version("1.0.5", md5="662e1914abbafe96087c61d8acc0641f")

	depends_on("r-matrixeqtl", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
