# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenlib(RPackage):
	"""Genealogical Data Analysis

	Genealogical data analysis including descriptive statistics (e.g., kinship and inbreeding coefficients) and gene-dropping simulations. See: "GENLIB: an R package for the analysis of genealogical data" Gauvin et al. (2015) <doi:10.1186/s12859-015-0581-5>.
	"""
	
	cran = "GENLIB" 

	version("1.1.10", md5="92679de1dd67a40d2dd704b886d5c779")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
