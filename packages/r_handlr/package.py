# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHandlr(RPackage):
	"""Convert Among Citation Formats

	Converts among many citation formats, including 'BibTeX',
    'Citeproc', 'Codemeta', 'RDF XML', 'RIS', 'Schema.org', and
    'Citation File Format'. A low level 'R6' class is provided, as well
    as stand-alone functions for each citation format for both read
    and write.
	"""
	
	homepage = "https://github.com/ropensci/handlr"
	cran = "handlr" 

	version("0.3.0", md5="b7ef6c560cc0f96eab49d57c2b9ec7dc")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
