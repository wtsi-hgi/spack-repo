# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDixontest(RPackage):
	"""Dixon's Ratio Test for Outlier Detection

	For outlier detection in small and normally distributed 
    samples the ratio test of Dixon (Q-test) can be used. Density,
    distribution function, quantile function and random generation 
    for Dixon's ratio statistics are provided as wrapper functions.
    The core applies McBane's Fortran functions <doi:10.18637/jss.v016.i03> 
    that use Gaussian quadrature for a numerical solution.
	"""
	
	cran = "dixonTest" 

	version("1.0.4", md5="3f0dfa902dc3f22986b729f500f9ac63")

