# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighdmean(RPackage):
	"""Testing Two-Sample Mean in High Dimension

	Implements the high-dimensional two-sample test 
    proposed by Zhang (2019) <http://hdl.handle.net/2097/40235>. 
    It also implements the test proposed by Srivastava, Katayama, 
    and Kano (2013) <doi:10.1016/j.jmva.2012.08.014>. These tests 
    are particularly suitable to high dimensional data from two populations 
    for which the classical multivariate Hotelling's T-square test fails due 
    to sample sizes smaller than dimensionality. In this case, the ZWL and ZWLm 
    tests proposed by Zhang (2019) <http://hdl.handle.net/2097/40235>, 
    referred to as zwl_test() in this package, provide a reliable and powerful test. 
	"""
	
	cran = "highDmean" 

	version("0.1.0", md5="ed359f20e582bf3989e1d02c609656eb")

	depends_on("r@3.1:", type=("build", "run"))
