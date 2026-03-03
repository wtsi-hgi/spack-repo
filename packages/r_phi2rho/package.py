# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhi2rho(RPackage):
	"""Owen's T Function and Bivariate Normal Integral

	Computes the Owen's T function or the bivariate
             normal integral using one of the following:
             modified Euler's arctangent series, tetrachoric
             series, or Vasicek's series.  For the methods,
             see Komelj, J. (2023) <doi:10.4236/ajcm.2023.134026>
             (or reprint <arXiv:2312.00011> with better typography)
             and Vasicek, O. A. (1998) <doi:10.21314/JCF.1998.015>.
	"""
	
	cran = "Phi2rho" 

	version("1.0.1", md5="e521cb19c2536c0f6c5a9af5a24bb2d5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
