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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rols_2.30.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rols/rols_2.30.2.tar.gz"]

	version("2.30.2", sha256="4b00441519faf003030c2deec30f4c1a6299a58e79a4ebc47a485cacc39519ba")

	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.23.1:", type=("build", "run"))
