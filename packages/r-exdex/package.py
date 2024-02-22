# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExdex(RPackage):
	"""Estimation of the Extremal Index

	Performs frequentist inference for the extremal index of a 
    stationary time series.  Two types of methodology are used.  One type is
    based on a model that relates the distribution of block maxima to the 
    marginal distribution of series and leads to the semiparametric maxima 
    estimators described in Northrop (2015) <doi:10.1007/s10687-015-0221-5> and 
    Berghaus and Bucher (2018) <doi:10.1214/17-AOS1621>.  Sliding block maxima
    are used to increase precision of estimation. A graphical block size 
    diagnostic is provided.  The other type of methodology uses a model for the 
    distribution of threshold inter-exceedance times (Ferro and Segers (2003) 
    <doi:10.1111/1467-9868.00401>). Three versions of this type of approach are 
    provided: the iterated weight least squares approach of Suveges (2007) 
    <doi:10.1007/s10687-007-0034-2>, the K-gaps model of 
    Suveges and Davison (2010) <doi:10.1214/09-AOAS292> and a similar approach
    of Holesovsky and Fusek (2020) <doi:10.1007/s10687-020-00374-3> 
    that we refer to as D-gaps. For the K-gaps and D-gaps models this package 
    allows missing values in the data, can accommodate independent subsets of 
    data, such as monthly or seasonal time series from different years, and can 
    incorporate information from right-censored inter-exceedance times.  
    Graphical diagnostics for the threshold level and the respective tuning
    parameters K and D are provided.
	"""
	
	homepage = "https://github.com/paulnorthrop/exdex"
	cran = "exdex" 

	version("1.2.3", md5="a30891a6c53ec03fa527562dedba2b2f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-chandwich", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
