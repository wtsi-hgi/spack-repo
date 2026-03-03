# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiblioverlap(RPackage):
	"""Document-Level Matching Between Bibliographic Datasets

	Identifies and visualizes document overlap in any number of bibliographic datasets.
    This package implements the identification of overlapping documents through the exact match of a unique 
    identifier (e.g. Digital Object Identifier - DOI) and, for records where the identifier is absent, through a score calculated 
    from a set of fields commonly found in bibliographic datasets (Title, Source, Authors and Publication Year).
    Additionally, it provides functions to visualize the results of the document matching through a Venn diagram 
    and/or UpSet plot, as well as a summary of the matching procedure. 
	"""
	
	homepage = "https://github.com/gavieira/biblioverlap"
	cran = "biblioverlap" 

	version("1.0.2", md5="df0f674feb0787233f12d31ba5405eea")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggvenndiagram", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
