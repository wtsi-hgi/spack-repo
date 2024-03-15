# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtom4r(RPackage):
	"""Tools to Handle and Publish Metadata as 'Atom' XML Format

	Provides tools to read/write/publish metadata based on the 'Atom' XML syndication format. This includes
 support of 'Dublin Core' XML implementation, and a client to API(s) implementing the 'AtomPub' 'SWORD' API specification.
	"""
	
	homepage = "https://github.com/eblondel/atom4R"
	cran = "atom4R" 

	version("0.3-3", md5="92d382af705bc62b2e419bd16db6bb78")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-rdflib", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
