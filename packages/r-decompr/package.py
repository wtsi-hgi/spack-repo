# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecompr(RPackage):
	"""Global Value Chain Decomposition

	Three global value chain (GVC) decompositions are implemented. 
    The Leontief decomposition derives the value added origin of exports by 
    country and industry as in Hummels, Ishii and Yi (2001). The Koopman, 
    Wang and Wei (2014) decomposition splits country-level exports into 9 
    value added components, and the Wang, Wei and Zhu (2013) decomposition 
    splits bilateral exports into 16 value added components. Various GVC 
    indicators based on these decompositions are computed in the 
    complimentary 'gvc' package. 
    --- References: ---
    Hummels, D., Ishii, J., & Yi, K. M. (2001). The nature and growth of 
       vertical specialization in world trade. Journal of international 
       Economics, 54(1), 75-96.
    Koopman, R., Wang, Z., & Wei, S. J. (2014). Tracing value-added and double 
       counting in gross exports. American Economic Review, 104(2), 459-94.
    Wang, Z., Wei, S. J., & Zhu, K. (2013). Quantifying international production 
       sharing at the bilateral and sector levels (No. w19677). 
       National Bureau of Economic Research.
	"""
	
	homepage = "https://qua.st/decompr/"
	cran = "decompr" 

	version("6.4.0", md5="481e5205d9a8fef0ca165e40a46f6681")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
