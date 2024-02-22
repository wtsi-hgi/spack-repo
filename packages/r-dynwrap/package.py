# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynwrap(RPackage):
	"""Representing and Inferring Single-Cell Trajectories

	Provides functionality to infer trajectories from single-cell data,
  represent them into a common format, and adapt them. Other biological information
  can also be added, such as cellular grouping, RNA velocity and annotation.
  Saelens et al. (2019) <doi:10.1038/s41587-019-0071-9>.
	"""
	
	homepage = "https://github.com/dynverse/dynwrap"
	cran = "dynwrap" 

	version("1.2.4", md5="35307b85281bf3bd0d098db32d0f1d10")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-babelwhale", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dynutils@1.0.3:", type=("build", "run"))
	depends_on("r-dynparam", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
