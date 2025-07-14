# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneclassifiers(RPackage):
	"""Application of gene classifiers

	This packages aims for easy accessible application of classifiers which have been published in literature using an ExpressionSet as input.
	"""
	
	homepage = "https://doi.org/doi:10.18129/B9.bioc.geneClassifiers"
	bioc = "geneClassifiers" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/geneClassifiers_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/geneClassifiers/geneClassifiers_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="f5a45f5b24da69f0879075ae5aae2f469c2e220d13bb47fa2eb95f8516fb7f1f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
