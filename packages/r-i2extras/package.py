# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RI2extras(RPackage):
	"""Functions to Work with 'incidence2' Objects

	Provides functions to work with 'incidence2' objects, including a
  simplified interface for trend fitting and peak estimation. This package is
  part of the RECON (<https://www.repidemicsconsortium.org/>) toolkit for 
  outbreak analysis (<https://www.reconverse.org/).
	"""
	
	homepage = "https://www.reconverse.org/i2extras/"
	cran = "i2extras" 

	version("0.2.1", md5="6efc707cdac2467ade928aada8127415")

	depends_on("r-incidence2@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-citools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
