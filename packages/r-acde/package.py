# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcde(RPackage):
	"""Artificial Components Detection of Differentially Expressed Genes.

	This package provides a multivariate inferential analysis method for
	detecting differentially expressed genes in gene expression data. It
	uses artificial components, close to the data's principal components but
	with an exact interpretation in terms of differential genetic
	expression, to identify differentially expressed genes while controlling
	the false discovery rate (FDR). The methods on this package are
	described in the vignette or in the article 'Multivariate Method for
	Inferential Identification of Differentially Expressed Genes in Gene
	Expression Experiments' by J. P. Acosta, L. Lopez-Kleine and S. Restrepo
	(2015, pending publication)."""

	bioc = "acde"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/acde_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/acde/acde_1.32.0.tar.gz"]

	version("1.32.0", md5="9a324caddfceb2aa977e0fc9e7e41615")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-boot@1.3:", type=("build", "run"))
