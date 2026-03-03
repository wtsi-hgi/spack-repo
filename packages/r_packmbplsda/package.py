# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackmbplsda(RPackage):
	"""Multi-Block Partial Least Squares Discriminant Analysis

	Several functions are provided to implement a MBPLSDA : components search, optimal model components number search, optimal model validity test by permutation tests, observed values evaluation of optimal model parameters and predicted categories, bootstrap values evaluation of optimal model parameters and predicted cross-validated categories. The use of this package is described in Brandolini-Bunlon et al (2019. Multi-block PLS discriminant analysis for the joint analysis of metabolomic and epidemiological data. Metabolomics, 15(10):134).
	"""
	
	cran = "packMBPLSDA" 

	version("0.9.0", md5="9c4ca09eedd21a41383732c8dedf0e1b")

	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
