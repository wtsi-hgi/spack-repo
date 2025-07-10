# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniprotkeywords(RPackage):
	"""Keywords from UniProt Database

	UniProt database provides a list of controlled vocabulary represented as keywords for genes or proteins. This is useful for summarizing gene functions in a compact way. This package provides data of keywords hierarchy and gene-keyword relations.
	"""
	
	homepage = "https://github.com/jokergoo/UniProtKeywords"
	bioc = "UniProtKeywords" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/UniProtKeywords_0.99.7.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/UniProtKeywords/UniProtKeywords_0.99.7.tar.gz"]

	version("0.99.7", sha256="f84bd81163f7ed48af39199f213a2a0cc7093f2af312728f578cad2a26152d82")

	depends_on("r@4:", type=("build", "run"))

