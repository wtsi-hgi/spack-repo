# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidypmc(RPackage):
	"""Parse Full Text XML Documents from PubMed Central

	Parse XML documents from the Open Access subset of Europe PubMed Central <https://europepmc.org>
    including section paragraphs, tables, captions and references.
	"""
	
	homepage = "https://github.com/cstubben/tidypmc"
	cran = "tidypmc" 

	version("1.7", md5="7407bc46eddbf8ea59f3cabb32cc7526")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
