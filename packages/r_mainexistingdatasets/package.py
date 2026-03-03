# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMainexistingdatasets(RPackage):
	"""Main Existing Human Datasets

	Shiny for Open Science to visualize, share, and inventory the
    main existing human datasets for researchers.
	"""
	
	cran = "MainExistingDatasets" 

	version("1.0.2", md5="5db00d5f94c0fcfce659cfc62408045b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
	depends_on("r-tmaptools", type=("build", "run"))
