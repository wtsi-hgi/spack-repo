# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKader(RPackage):
	"""Kernel Adaptive Density Estimation and Regression

	Implementation of various kernel adaptive methods in nonparametric curve
    estimation like density estimation as introduced in Stute and Srihera (2011)
    <doi:10.1016/j.spl.2011.01.013> and Eichner and Stute (2013)
    <doi:10.1016/j.jspi.2012.03.011> for pointwise estimation, and like regression
    as described in Eichner and Stute (2012) <doi:10.1080/10485252.2012.760737>.
	"""
	
	homepage = "http://github.com/GerritEichner/kader"
	cran = "kader" 

	version("0.0.8", md5="d47c88f164198490a64234f9159b17af")

	depends_on("r@3.4.1:", type=("build", "run"))
