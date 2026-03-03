# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWdm(RPackage):
	"""Weighted Dependence Measures

	Provides efficient implementations of weighted dependence measures
  and related asymptotic tests for independence. Implemented measures are
  the Pearson correlation, Spearman's rho, Kendall's tau, Blomqvist's beta, and
  Hoeffding's D; see, e.g., Nelsen (2006) <doi:10.1007/0-387-28678-0> and
  Hollander et al. (2015, ISBN:9780470387375).
	"""
	
	homepage = "https://github.com/tnagler/wdm-r"
	cran = "wdm" 

	version("0.2.4", md5="53467d0a74a2b78738d526fe078996d9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
