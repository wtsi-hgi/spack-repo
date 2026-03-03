# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompoissonreg(RPackage):
	"""Conway-Maxwell Poisson (COM-Poisson) Regression

	Fit Conway-Maxwell Poisson (COM-Poisson or CMP) regression models
    to count data (Sellers & Shmueli, 2010) <doi:10.1214/09-AOAS306>. The
    package provides functions for model estimation, dispersion testing, and
    diagnostics. Zero-inflated CMP regression (Sellers & Raim, 2016)
    <doi:10.1016/j.csda.2016.01.007> is also supported.
	"""
	
	homepage = "https://github.com/lotze/COMPoissonReg"
	cran = "COMPoissonReg" 

	version("0.8.1", md5="3a2d66982840e75e09321a7b2f9a8ea6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
