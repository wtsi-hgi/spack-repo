# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLax(RPackage):
	"""Loglikelihood Adjustment for Extreme Value Models

	Performs adjusted inferences based on model objects fitted, using 
    maximum likelihood estimation, by the extreme value analysis packages
    'eva' <https://cran.r-project.org/package=eva>, 
    'evd' <https://cran.r-project.org/package=evd>, 
    'evir' <https://cran.r-project.org/package=evir>, 
    'extRemes' <https://cran.r-project.org/package=extRemes>, 
    'fExtremes' <https://cran.r-project.org/package=fExtremes>, 
    'ismev' <https://cran.r-project.org/package=ismev>, 
    'mev' <https://cran.r-project.org/package=mev>, 
    'POT' <https://cran.r-project.org/package=POT> and
    'texmex' <https://cran.r-project.org/package=texmex>. 
    Adjusted standard errors and an adjusted loglikelihood are provided, using    
    the 'chandwich' package <https://cran.r-project.org/package=chandwich>
    and the object-oriented features of the 'sandwich' package 
    <https://cran.r-project.org/package=sandwich>. The adjustment is based on a 
    robust sandwich estimator of the parameter covariance matrix, based on the 
    methodology in Chandler and Bate (2007) <doi:10.1093/biomet/asm015>. This 
    can be used for cluster correlated data when interest lies in the 
    parameters of the marginal distributions, or for performing inferences that 
    are robust to certain types of model misspecification.  Univariate extreme 
    value models, including regression models, are supported.  
	"""
	
	homepage = "https://paulnorthrop.github.io/lax/"
	cran = "lax" 

	version("1.2.3", md5="34231581360c96b6696148c381889c9e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-chandwich", type=("build", "run"))
	depends_on("r-exdex", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-revdbayes", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
