# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXdcclarge(RPackage):
	"""Estimating a (c)DCC-GARCH Model in Large Dimensions

	Functions for Estimating a (c)DCC-GARCH Model in large dimensions
    based on a publication by Engle et,al (2017) <doi:10.1080/07350015.2017.1345683> and Nakagawa et,al (2018) <doi:10.3390/ijfs6020052>.
    This estimation method is consist of composite likelihood method by Pakel et al. (2014) <http://paneldataconference2015.ceu.hu/Program/Cavit-Pakel.pdf>
    and (Non-)linear shrinkage estimation of covariance matrices by Ledoit and Wolf (2004,2015,2016). (<doi:10.1016/S0047-259X(03)00096-4>,
    <doi:10.1214/12-AOS989>, <doi:10.1016/j.jmva.2015.04.006>).
	"""
	
	cran = "xdcclarge" 

	version("0.1.0", md5="5cfec1c78229c7a70d2f165b18622252")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.10.6:", type=("build", "run"))
	depends_on("r-nlshrink", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.2.34:", type=("build", "run"))
