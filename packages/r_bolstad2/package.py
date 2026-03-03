# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBolstad2(RPackage):
	"""Bolstad Functions

	A set of R functions and data sets for the book "Understanding Computational Bayesian Statistics." This book was written by Bill (WM) Bolstad and published in 2009 by John Wiley & Sons (ISBN 978-0470046098).
	"""
	
	homepage = "https://github.com/jmcurran/Bolstad2"
	cran = "Bolstad2" 

	version("1.0-29", md5="cb2522edfb084b64285ffc082d898acf", url="https://cran.r-project.org/src/contrib/Bolstad2_1.0-29.tar.gz")

