# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidytlg(RPackage):
	"""Create TLGs using the 'tidyverse'

	Generate tables, listings, and graphs (TLG) using 'tidyverse.'
  Tables can be created functionally, using a standard TLG process, or by
  specifying table and column metadata to create generic analysis summaries.
  The 'envsetup' package can also be leveraged to create environments for table
  creation.
	"""
	
	homepage = "https://github.com/pharmaverse/tidytlg"
	cran = "tidytlg" 

	version("0.1.4", md5="67368dfcb8d2fffcfe9b0017bf216b18")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-forcats@0.5.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-huxtable@5.1:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-usethis@1.6.3:", type=("build", "run"))
	depends_on("r-crayon@1.4.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-cellranger@1.1:", type=("build", "run"))
	depends_on("r-png@0.1.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
