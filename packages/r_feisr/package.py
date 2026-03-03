# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeisr(RPackage):
	"""Estimating Fixed Effects Individual Slope Models

	Provides the function feis() to estimate fixed effects individual 
    slope (FEIS) models. The FEIS model constitutes a more general version of 
    the often-used fixed effects (FE) panel model, as implemented in the 
    package 'plm' by Croissant and Millo (2008) <doi:10.18637/jss.v027.i02>. 
    In FEIS models, data are not only person demeaned like in conventional 
    FE models, but detrended by the predicted individual slope of each 
    person or group. Estimation is performed by applying least squares lm() 
    to the transformed data. For more details on FEIS models see Bruederl and 
    Ludwig (2015, ISBN:1446252442); Frees (2001) <doi:10.2307/3316008>; 
    Polachek and Kim (1994) <doi:10.1016/0304-4076(94)90075-2>; 
	Ruettenauer and Ludwig (2020) <doi:10.1177/0049124120926211>;
    Wooldridge (2010, ISBN:0262294354). To test consistency of conventional FE 
    and random effects estimators against heterogeneous slopes, the package 
    also provides the functions feistest() for an artificial regression test 
    and bsfeistest() for a bootstrapped version of the Hausman test.
	"""
	
	homepage = "https://github.com/ruettenauer/feisr"
	cran = "feisr" 

	version("1.3.0", md5="50fc7fc19a331306573148b48aae5f16")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
