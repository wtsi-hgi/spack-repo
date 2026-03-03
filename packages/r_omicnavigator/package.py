# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicnavigator(RPackage):
	"""Open-Source Software for 'Omic' Data Analysis and Visualization

	
  A tool for interactive exploration of the results from 'omics'
  experiments to facilitate novel discoveries from high-throughput biology. The
  software includes R functions for the 'bioinformatician' to deposit study
  metadata and the outputs from statistical analyses (e.g. differential
  expression, enrichment). These results are then exported to an interactive
  JavaScript dashboard that can be interrogated on the user's local machine or
  deployed online to be explored by collaborators. The dashboard includes
  'sortable' tables, interactive plots including network visualization, and
  fine-grained filtering based on statistical significance.
	"""
	
	homepage = "https://github.com/abbvie-external/OmicNavigator"
	cran = "OmicNavigator" 

	version("1.13.13", md5="409858dcd3aa90fac98de4791a90422b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
