# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofgamma(RPackage):
	"""Goodness-of-Fit Tests for the Gamma Distribution

	We implement various classical tests for the composite hypothesis of testing the fit to the family of gamma distributions as the Kolmogorov-Smirnov test, the Cramer-von Mises test, the Anderson Darling test and the Watson test. For each test a parametric bootstrap procedure is implemented, as considered in Henze, Meintanis & Ebner (2012) <doi:10.1080/03610926.2010.542851>. The recent procedures presented in Henze, Meintanis & Ebner (2012) <doi:10.1080/03610926.2010.542851> and Betsch & Ebner (2019) <doi:10.1007/s00184-019-00708-7> are implemented. Estimation of parameters of the gamma law are implemented using the method of Bhattacharya (2001) <doi:10.1080/00949650108812100>. 
	"""
	
	cran = "gofgamma" 

	version("1.0", md5="0c67f350b597cc0fef8e2703cdcce27f")

	depends_on("r@3.5:", type=("build", "run"))
