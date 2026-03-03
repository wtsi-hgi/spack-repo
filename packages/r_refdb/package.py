# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefdb(RPackage):
	"""A DNA Reference Library Manager

	Reference database manager offering a set of functions
    to import, organize, clean, filter, audit and export reference genetic
    data. Provide functions to download sequence data from
    Bold Systems (<https://www.boldsystems.org/>) and
    NCBI GenBank <https://www.ncbi.nlm.nih.gov/genbank/>.
    Designed as an environment for semi-automatic and assisted
    construction of reference databases and to improve standardization
    and repeatability in barcoding and metabarcoding studies.
	"""
	
	homepage = "https://fkeck.github.io/refdb/"
	cran = "refdb" 

	version("0.1.1", md5="65128a665fc4a6e8ccfec5190671ab00")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-bold", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-bioseq", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
