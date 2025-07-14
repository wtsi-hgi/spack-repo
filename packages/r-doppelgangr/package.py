# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoppelgangr(RPackage):
	"""Identify likely duplicate samples from genomic or meta-data

	The main function is doppelgangR(), which takes as minimal input a list of ExpressionSet object, and searches all list pairs for duplicated samples.  The search is based on the genomic data (exprs(eset)), phenotype/clinical data (pData(eset)), and "smoking guns" - supposedly unique identifiers found in pData(eset).
	"""
	
	homepage = "https://github.com/lwaldron/doppelgangR"
	bioc = "doppelgangR"

	version("1.36.1", commit="210026ae61c976af99c672c96f913d9e300bb11b")
	version("1.30.0", commit="2f9209ec4fc154b77816d0aae966dc4b9b43ee5c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
