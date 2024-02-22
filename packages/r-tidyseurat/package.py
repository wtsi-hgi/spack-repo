# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyseurat(RPackage):
	"""Brings Seurat to the Tidyverse

	It creates an invisible layer that allow to see the 'Seurat' object 
    as tibble and interact seamlessly with the tidyverse.
	"""
	
	homepage = "https://github.com/stemangiola/tidyseurat"
	cran = "tidyseurat" 

	version("0.8.0", md5="844d068094e1d6b8e025cddc65eb336b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ttservice@0.3.8:", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
	depends_on("r-seurat@4.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
