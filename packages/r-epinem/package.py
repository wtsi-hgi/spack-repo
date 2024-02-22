# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpinem(RPackage):
	"""epiNEM

	epiNEM is an extension of the original Nested Effects Models (NEM). EpiNEM is able to take into account double knockouts and infer more complex network signalling pathways. It is tailored towards large scale double knock-out screens.
	"""
	
	homepage = "https://github.com/cbg-ethz/epiNEM/"
	bioc = "epiNEM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/epiNEM_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/epiNEM/epiNEM_1.26.0.tar.gz"]

	version("1.26.0", md5="03702ef94f047496994ebaf19f750787")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-boolnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-mnem", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
