# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKfigr(RPackage):
	"""Integrated Code Chunk Anchoring and Referencing for R Markdown
Documents

	A streamlined cross-referencing system for R Markdown documents
    generated with 'knitr'. R Markdown is  an authoring format for generating
    dynamic content from R. 'kfigr' provides a hook for anchoring code
    chunks and a function to cross-reference document elements generated from
    said chunks, e.g. figures and tables.
	"""
	
	homepage = "https://github.com/mkoohafkan/kfigr"
	cran = "kfigr" 

	version("1.2.1", md5="b48c0fbec34085b71363d02c8b0449c4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-knitr@1.6:", type=("build", "run"))
