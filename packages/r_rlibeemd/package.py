# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlibeemd(RPackage):
	"""Ensemble Empirical Mode Decomposition (EEMD) and Its Complete
Variant (CEEMDAN)

	An R interface for libeemd (Luukko, Helske, Räsänen, 2016) <doi:10.1007/s00180-015-0603-9>, 
    a C library of highly efficient parallelizable functions  for performing the ensemble empirical mode decomposition (EEMD), 
    its complete variant (CEEMDAN), the regular empirical mode decomposition (EMD), and bivariate EMD (BEMD). 
    Due to the possible portability issues CRAN version no longer supports OpenMP, you can install OpenMP-supported version 
    from GitHub: <https://github.com/helske/Rlibeemd/>.
	"""
	
	cran = "Rlibeemd" 

	version("1.4.3", md5="5144847579b8691c06537d48af98207f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
