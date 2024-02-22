# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmallcountrounding(RPackage):
	"""Small Count Rounding of Tabular Data

	A statistical disclosure control tool to protect frequency tables in cases where small values are sensitive. The function PLSrounding() performs small count rounding of necessary inner cells so that all small frequencies of cross-classifications to be published (publishable cells) are rounded. This is equivalent to changing micro data since frequencies of unique combinations are changed. Thus, additivity and consistency are guaranteed. The methodology is described in Langsrud and Heldal (2018) <https://www.researchgate.net/publication/327768398_An_Algorithm_for_Small_Count_Rounding_of_Tabular_Data>.
	"""
	
	homepage = "https://github.com/statisticsnorway/SmallCountRounding"
	cran = "SmallCountRounding" 

	version("1.0.3", md5="aa4bfb684601ac5070ee04dda08f6c6e")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ssbtools@1.3.4:", type=("build", "run"))
