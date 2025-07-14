# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRols(RPackage):
	"""An R interface to the Ontology Lookup Service

	The rols package is an interface to the Ontology Lookup Service (OLS) to access and query hundred of ontolgies directly from R.
	"""
	
	homepage = "http://lgatto.github.io/rols/"
	bioc = "rols"

	version("3.4.0", commit="c420652788760b5781c4eeffcb45f1e672c40dd7")
	version("2.30.2", commit="8b7efefc3038c430adba2c56a2e21227b3da5d3d")

	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.23.1:", type=("build", "run"))
