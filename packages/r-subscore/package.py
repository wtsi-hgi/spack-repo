# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubscore(RPackage):
	"""Computing Subscores in Classical Test Theory and Item Response
Theory

	Functions for computing test subscores using different
    methods in both classical test theory (CTT) and item response theory (IRT). This
    package enables three types of subscoring methods within the framework of CTT
    and IRT, including (1) Wainer's augmentation method (Wainer et. al., 2001) 
    <doi:10.4324/9781410604729>, (2) Haberman's subscoring methods (Haberman, 2008) 
    <doi:10.3102/1076998607302636>, and (3) Yen's objective performance index (OPI; Yen, 1987) 
    <https://www.ets.org/research/policy_research_reports/publications/paper/1987/hrap>. 
    It also includes functions to compute Proportional Reduction 
    of Mean Squared Errors (PRMSEs) in Haberman's methods which are used to 
    examine whether test subscores are of added value. In addition, the package includes 
    a function to assess the local independence assumption of IRT with
    Yen's Q3 statistic (Yen, 1984 <doi:10.1177/014662168400800201>; Yen, 1993 
    <doi:10.1111/j.1745-3984.1993.tb00423.x>).
	"""
	
	cran = "subscore" 

	version("3.3", md5="e4dc29c6b45fe44dc5b56bb8b9d704fb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ctt", type=("build", "run"))
	depends_on("r-irtoys", type=("build", "run"))
	depends_on("r-sirt", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-cocor", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
