# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowmatch(RPackage):
	"""Matching and meta-clustering in flow cytometry

	Matching cell populations and building meta-clusters and templates from a collection of FC samples.
	"""
	
	bioc = "flowMatch" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowMatch_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowMatch/flowMatch_1.38.0.tar.gz"]

	version("1.38.0", md5="78b2b9dc87eec35dbc65c59dadb1ffd9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
