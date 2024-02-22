# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodemetar(RPackage):
	"""Generate 'CodeMeta' Metadata for R Packages

	The 'Codemeta' Project defines a 'JSON-LD' format
    for describing software metadata, as detailed at
    <https://codemeta.github.io>. This package provides utilities to
    generate, parse, and modify 'codemeta.json' files automatically for R
    packages, as well as tools and examples for working with
    'codemeta.json' 'JSON-LD' more generally.
	"""
	
	homepage = "https://github.com/ropensci/codemetar"
	cran = "codemetar" 

	version("0.3.5", md5="bd704c61e07626186fe4aa3e8c7aadc0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-commonmark", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-codemeta", type=("build", "run"))
