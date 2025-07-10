# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGispa(RPackage):
	"""GISPA: Method for Gene Integrated Set Profile Analysis

	GISPA is a method intended for the researchers who are interested in defining gene sets with similar, a priori specified molecular profile. GISPA method has been previously published in Nucleic Acid Research (Kowalski et al., 2016; PMID: 26826710).
	"""
	
	bioc = "GISPA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GISPA_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GISPA/GISPA_1.26.0.tar.gz"]

	version("1.26.0", sha256="9f0edb08e51e9e8a86d06cd3fc5b303d7985878c67e8f6a6d13d95e49a636ba7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-hh", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
