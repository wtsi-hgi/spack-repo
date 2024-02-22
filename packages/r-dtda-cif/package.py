# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtdaCif(RPackage):
	"""Doubly Truncated Data Analysis, Cumulative Incidence Functions

	Nonparametric estimator of the cumulative incidences of competing risks under double truncation. The estimator generalizes the Efron-Petrosian NPMLE (Non-Parametric Maximun Likelihood Estimator) to the competing risks setting. Efron, B. and Petrosian, V. (1999) <doi:10.2307/2669997>. 
	"""
	
	cran = "DTDA.cif" 

	version("1.0.2", md5="38688e0171772a9bff2bfd1df6e939ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
