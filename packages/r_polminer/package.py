# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolminer(RPackage):
	"""Verbs and Nouns for Corpus Analysis

	Package for corpus analysis using the Corpus Workbench 
    ('CWB', <https://cwb.sourceforge.io>) as an efficient back end for indexing
    and querying large corpora. The package offers functionality to flexibly create
    subcorpora and to carry out basic statistical operations (count, co-occurrences
    etc.). The original full text of documents can be reconstructed and inspected at
    any time. Beyond that, the package is intended to serve as an interface to 
    packages implementing advanced statistical procedures. Respective data structures
    (document-term matrices, term-co-occurrence matrices etc.) can be created based 
    on the indexed corpora.
	"""
	
	homepage = "https://github.com/PolMine/polmineR"
	cran = "polmineR" 

	version("0.8.9", md5="8fba2cf0f32688e232cd968d726ccbab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcppcwb@0.6.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
