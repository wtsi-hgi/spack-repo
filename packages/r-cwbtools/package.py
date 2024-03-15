# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCwbtools(RPackage):
	"""Tools to Create, Modify and Manage 'CWB' Corpora

	The 'Corpus Workbench' ('CWB', <https://cwb.sourceforge.io/>) offers a classic and mature
 approach for working with large, linguistically and structurally annotated corpora. The 'CWB'
 is memory efficient and its design makes running queries fast, see Evert (2011)
 <https://eprints.lancs.ac.uk/id/eprint/62721>. The 'cwbtools' package offers
 pure 'R' tools to create indexed corpus files as well as high-level wrappers for the original 'C'
 implementation of 'CWB' as exposed by the 'RcppCWB' package
 (<https://CRAN.R-project.org/package=RcppCWB>). Additional functionality to add and
 modify annotations of corpora from within 'R' makes working with 'CWB' indexed corpora
 much more flexible and convenient. The 'cwbtools' package in combination with the 'R' packages
 'RcppCWB' (<https://CRAN.R-project.org/package=RcppCWB>) and 'polmineR'
 (<https://CRAN.R-project.org/package=polmineR>) offers a lightweight infrastructure
 to support the combination of quantitative and qualitative approaches for working
 with textual data.
	"""
	
	homepage = "https://github.com/PolMine/cwbtools"
	cran = "cwbtools" 

	version("0.4.0", md5="3cb73899b38c4ac8454bb1b75be9e6e4")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rcppcwb@0.6.3:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-zen4r@0.9:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
