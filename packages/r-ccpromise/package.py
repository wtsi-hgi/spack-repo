# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcpromise(RPackage):
	"""PROMISE analysis with Canonical Correlation for Two Forms of High Dimensional Genetic Data

	Perform Canonical correlation between two forms of high demensional genetic data, and associate the first compoent of each form of data with a specific biologically interesting pattern of associations with multiple endpoints. A probe level analysis is also implemented.
	"""
	
	bioc = "CCPROMISE" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CCPROMISE_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CCPROMISE/CCPROMISE_1.28.0.tar.gz"]

	version("1.28.0", md5="1b85c7bbed3be474abf4e4591882abdf")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ccp", type=("build", "run"))
	depends_on("r-promise", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
