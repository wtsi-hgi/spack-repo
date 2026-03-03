# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvdoctr(RPackage):
	"""Ensures Mutually Consistent Beliefs When Using IVs

	Uses data and researcher's beliefs on measurement error and
    instrumental variable (IV) endogeneity to generate the space of consistent 
    beliefs across measurement error, instrument endogeneity, and instrumental 
    relevance for IV regressions. 
    Package based on DiTraglia and Garcia-Jimeno (2020) <doi:10.1080/07350015.2020.1753528>.
	"""
	
	cran = "ivdoctr" 

	version("1.0.1", md5="6e2a23cad616414511790181bbf1d60f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
