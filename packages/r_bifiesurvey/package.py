# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBifiesurvey(RPackage):
	"""Tools for Survey Statistics in Educational Assessment

	
    Contains tools for survey statistics (especially in educational
    assessment) for datasets with replication designs (jackknife, 
    bootstrap, replicate weights; see Kolenikov, 2010;
    Pfefferman & Rao, 2009a, 2009b, <doi:10.1016/S0169-7161(09)70003-3>,
    <doi:10.1016/S0169-7161(09)70037-9>); Shao, 1996, 
    <doi:10.1080/02331889708802523>). 
    Descriptive statistics, linear and logistic regression, 
    path models for manifest variables with measurement error 
    correction and two-level hierarchical regressions for weighted 
    samples are included. Statistical inference can be conducted for 
    multiply imputed datasets and nested multiply imputed datasets
    and is in particularly suited for the analysis of plausible values
    (for details see George, Oberwimmer & Itzlinger-Bruneforth, 2016; 
    Bruneforth, Oberwimmer & Robitzsch, 2016; Robitzsch, Pham &
    Yanagida, 2016). The package development was supported by BIFIE 
    (Federal Institute for Educational Research, Innovation and Development 
    of the Austrian School System; Salzburg, Austria).
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/BIFIEsurvey"
	cran = "BIFIEsurvey" 

	version("3.5-19", md5="196cd9318cef5d67e43a229d89ca3c18")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-miceadds", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
