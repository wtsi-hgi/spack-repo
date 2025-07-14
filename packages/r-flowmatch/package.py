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

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="30ac0a6442d25cc2df021cda9ca68d69dbfaf5272e26f734c48e7e2915e27cef")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
