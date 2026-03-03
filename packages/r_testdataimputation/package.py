# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestdataimputation(RPackage):
	"""Missing Item Responses Imputation for Test and Assessment Data

	Functions for imputing missing item responses for dichotomous and
    polytomous test and assessment data. This package enables missing imputation
    methods that are suitable for test and assessment data, including: 
    listwise (LW) deletion (see De Ayala et al. 2001 <doi:10.1111/j.1745-3984.2001.tb01124.x>), 
    treating as incorrect (IN, see Lord, 1974 <doi: 10.1111/j.1745-3984.1974.tb00996.x>; 
    Mislevy & Wu, 1996 <doi: 10.1002/j.2333-8504.1996.tb01708.x>; 
    Pohl et al., 2014 <doi: 10.1177/0013164413504926>), person mean imputation (PM), 
    item mean imputation (IM), two-way (TW) and response function (RF) imputation,
    (see Sijtsma & van der Ark, 2003 <doi: 10.1207/s15327906mbr3804_4>),
    logistic regression (LR) imputation, predictive mean matching (PMM), and expectation–maximization (EM) 
    imputation (see Finch, 2008 <doi: 10.1111/j.1745-3984.2008.00062.x>).
	"""
	
	cran = "TestDataImputation" 

	version("2.3", md5="1cd43b8b7519aeb868c20b4240f54b8b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-amelia", type=("build", "run"))
