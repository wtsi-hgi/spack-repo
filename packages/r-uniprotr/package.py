# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniprotr(RPackage):
	"""Retrieving Information of Proteins from Uniprot

	Connect to Uniprot <https://www.uniprot.org/> to retrieve information about proteins using their accession number such information could be name or taxonomy information, For detailed information kindly read the publication <https://www.sciencedirect.com/science/article/pii/S1874391919303859>.
	"""
	
	homepage = "https://github.com/Proteomicslab57357/UniprotR"
	cran = "UniprotR" 

	version("2.3.0", md5="0d4cb53e95c331a017f6490522673188")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-alakazam", type=("build", "run"))
	depends_on("r-gprofiler2", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
