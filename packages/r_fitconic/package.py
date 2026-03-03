# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitconic(RPackage):
	"""Fit Data to Any Conic Section

	Fit data to an ellipse, hyperbola, or parabola. Bootstrapping is available when needed. The conic curve can be rotated through an  arbitrary angle and the fit will still succeed. Helper functions are  provided to convert generator coefficients from one style to another, generate test data sets, rotate conic section parameters, and so on. References include Nikolai Chernov (2014) "Fitting ellipses, circles, and lines by  least squares" <https://people.cas.uab.edu/~mosya/cl/>; A. W. Fitzgibbon, M. Pilu, R. B. Fisher (1999) "Direct Least Squares Fitting of Ellipses" IEEE Trans. PAMI,  Vol. 21, pages 476-48; N. Chernov, Q. Huang, and H. Ma (2014) "Fitting quadratic curves to data points", British Journal of Mathematics & Computer Science, 4, 33-60; N. Chernov and H. Ma  (2011) "Least squares fitting of quadratic curves and surfaces", Computer Vision, Editor S. R. Yoshida, Nova Science Publishers, pp. 285-302.  
	"""
	
	cran = "fitConic" 

	version("1.2.1", md5="ff339b15db1765b1d82c9fe511211f4a")

	depends_on("r-pracma", type=("build", "run"))
