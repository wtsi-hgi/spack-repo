# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiceadds(RPackage):
	"""Some Additional Multiple Imputation Functions, Especially for
'mice'

	
    Contains functions for multiple imputation which
    complements existing functionality in R.
    In particular, several imputation methods for the
    mice package (van Buuren & Groothuis-Oudshoorn, 2011,
    <doi:10.18637/jss.v045.i03>) are implemented.
    Main features of the miceadds package include
    plausible value imputation (Mislevy, 1991,
    <doi:10.1007/BF02294457>), multilevel imputation for
    variables at any level or with any number of hierarchical
    and non-hierarchical levels (Grund, Luedtke & Robitzsch,
    2018, <doi:10.1177/1094428117703686>; van Buuren, 2018, 
    Ch.7, <doi:10.1201/9780429492259>), imputation using 
    partial least squares (PLS) for high dimensional 
    predictors (Robitzsch, Pham & Yanagida, 2016), 
    nested multiple imputation (Rubin, 2003, 
    <doi:10.1111/1467-9574.00217>), substantive model
    compatible imputation (Bartlett et al., 2015,
    <doi:10.1177/0962280214521348>), and features
    for the generation of synthetic datasets
    (Reiter, 2005, <doi:10.1111/j.1467-985X.2004.00343.x>;
    Nowok, Raab, & Dibben, 2016, <doi:10.18637/jss.v074.i11>).
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/miceadds"
	cran = "miceadds" 

	version("3.17-44", md5="f4bfee87c40821fe63fc503d17f81c77")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-mice@3:", type=("build", "run"))
	depends_on("r-mitools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
