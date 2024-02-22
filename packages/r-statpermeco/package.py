# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatpermeco(RPackage):
	"""Statistical Performance Measures to Evaluate Covariance Matrix
Estimates

	Statistical performance measures used in the econometric literature to evaluate conditional covariance/correlation matrix estimates (MSE, MAE, Euclidean distance, Frobenius distance, Stein distance, asymmetric loss function, eigenvalue loss function and the loss function defined in Eq. (4.6) of Engle et al. (2016) <doi:10.2139/ssrn.2814555>). Additionally, compute Eq. (3.1) and (4.2) of Li et al. (2016) <doi:10.1080/07350015.2015.1092975> to compare the factor loading matrix. The statistical performance measures implemented have been previously used in, for instance, Laurent et al. (2012) <doi:10.1002/jae.1248>,  Amendola et al. (2015) <doi:10.1002/for.2322> and  Becker et al. (2015) <doi:10.1016/j.ijforecast.2013.11.007>.
	"""
	
	cran = "StatPerMeCo" 

	version("0.1.0", md5="94c4dcf46c50266d125111934207e54d")

