# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpsettest(RPackage):
	"""A Set-Based Association Test using GWAS Summary Statistics

	The goal of 'snpsettest' is to provide simple tools that perform
             set-based association tests (e.g., gene-based association tests)
             using GWAS (genome-wide association study) summary statistics. A
             set-based association test in this package is based on the
             statistical model described in VEGAS (versatile gene-based
             association study), which combines the effects of a set of SNPs
             accounting for linkage disequilibrium between markers. This package
             uses a different approach from the original VEGAS implementation to
             compute set-level p values more efficiently, as described in
             <https://github.com/HimesGroup/snpsettest/wiki/Statistical-test-in-snpsettest>.
	"""
	
	homepage = "https://github.com/HimesGroup/snpsettest"
	cran = "snpsettest" 

	version("0.1.2", md5="ce2387ed8744ca7a73310e70a9286afe")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gaston", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
