# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZcurve(RPackage):
	"""An Implementation of Z-Curves

	An implementation of z-curves - a method for estimating expected discovery 
    and replicability rates on the bases of test-statistics of published studies. The package 
    provides functions for fitting the new density and EM version 
    (Bartoš & Schimmack, 2020, <doi:10.31234/osf.io/urgtn>), censored observations,  
    as well as the original density z-curve (Brunner & Schimmack, 2020, <doi:10.15626/MP.2018.874>). 
    Furthermore, the package provides summarizing and plotting functions for the fitted z-curve objects. 
    See the aforementioned articles for more information about the z-curves, expected discovery 
    and replicability rates, validation studies, and limitations.
	"""
	
	homepage = "https://fbartos.github.io/zcurve/"
	cran = "zcurve" 

	version("2.4.0", md5="d849885a8f9ff4bcf3b52fe4abf8e935")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-evmix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
