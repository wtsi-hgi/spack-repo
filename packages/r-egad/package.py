# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgad(RPackage):
	"""Extending guilt by association by degree

	The package implements a series of highly efficient tools to calculate functional properties of networks based on guilt by association methods.
	"""
	
	bioc = "EGAD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EGAD_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EGAD/EGAD_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="a53893dd4859052a7a2124f6a07da5e0961ee2bd35a20511dde1e59a10813b49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
