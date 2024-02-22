# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpqmpfr(RPackage):
	"""DPQ (Density, Probability, Quantile) Distribution Computations
using MPFR

	An extension to the 'DPQ' package with computations for 'DPQ'
  (Density (pdf), Probability (cdf) and Quantile) functions, where
  the functions here partly use the 'Rmpfr' package and hence the
  underlying 'MPFR' and 'GMP' C libraries.
	"""
	
	homepage = "https://specfun.r-forge.r-project.org/"
	cran = "DPQmpfr" 

	version("0.3-2", md5="f2bd5bc4b0ffca2e62096ea8d9d0a61f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dpq@0.5.3:", type=("build", "run"))
	depends_on("r-rmpfr@0.9.0:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
