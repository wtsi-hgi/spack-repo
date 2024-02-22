# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutbreaker2(RPackage):
	"""Bayesian Reconstruction of Disease Outbreaks by Combining
Epidemiologic and Genomic Data

	Bayesian reconstruction of disease outbreaks using epidemiological
    and genetic information. Jombart T, Cori A, Didelot X, Cauchemez S, Fraser
    C and Ferguson N. 2014. <doi:10.1371/journal.pcbi.1003457>. Campbell, F,
    Cori A, Ferguson N, Jombart T. 2019. <doi:10.1371/journal.pcbi.1006930>.
	"""
	
	cran = "outbreaker2" 

	version("1.1.3", md5="15fb80c18e5f12877b537ca1b547a61d", url="https://cran.r-project.org/src/contrib/outbreaker2_1.1.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
