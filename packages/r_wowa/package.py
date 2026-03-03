# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWowa(RPackage):
	"""Weighted Ordered Weighted Average

	Introduce weights into Ordered Weighted Averages and extend bivariate means based on n-ary tree construction. Please refer to the following:
	G. Beliakov, H. Bustince, and T. Calvo (2016, ISBN: 978-3-319-24753-3),
	G. Beliakov(2018) <doi:10.1002/int.21913>,
	G. Beliakov, J.J. Dujmovic (2016) <doi:10.1016/j.ins.2015.10.040>,
	J.J. Dujmovic and G. Beliakov (2017) <doi:10.1002/int.21828>.
	"""
	
	cran = "wowa" 

	version("1.0.2", md5="a0067fffcaf7764ce4107f16dca421e7")

	depends_on("r-rcpp", type=("build", "run"))
