# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModifiedmk(RPackage):
	"""Modified Versions of Mann Kendall and Spearman's Rho Trend Tests

	Power of non-parametric Mann-Kendall test and Spearman’s Rho test is highly influenced by serially correlated data. To address this issue, trend tests may be applied on the modified versions of the time series data by  Block Bootstrapping (BBS), Prewhitening (PW) , Trend Free Prewhitening (TFPW), Bias Corrected Prewhitening and Variance Correction Approach by calculating effective sample size.
    Mann, H. B. (1945).<doi:10.1017/CBO9781107415324.004>.
    Kendall, M. (1975). Multivariate analysis. Charles Griffin&Company Ltd,. 
    sen, P. K. (1968).<doi:10.2307/2285891>.
    Önöz, B., & Bayazit, M. (2012) <doi:10.1002/hyp.8438>.
    Hamed, K. H. (2009).<doi:10.1016/j.jhydrol.2009.01.040>.
    Yue, S., & Wang, C. Y. (2002) <doi:10.1029/2001WR000861>.
    Yue, S., Pilon, P., Phinney, B., & Cavadias, G. (2002) <doi:10.1002/hyp.1095>.
    Hamed, K. H., & Ramachandra Rao, A. (1998) <doi:10.1016/S0022-1694(97)00125-X>.
    Yue, S., & Wang, C. Y. (2004) <doi:10.1023/B:WARM.0000043140.61082.60>.
	"""
	
	cran = "modifiedmk" 

	version("1.6", md5="e464d26827af48151b2ed69cc8a60aef")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
