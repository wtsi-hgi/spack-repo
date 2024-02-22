# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyestimate(RPackage):
	"""A Tidy Implementation of 'ESTIMATE'

	The 'ESTIMATE' package infers tumor purity from expression data as a 
  function of immune and stromal infiltrate, but requires writing of intermediate 
  files, is un-pipeable, and performs poorly when presented with modern datasets 
  with current gene symbols. 'tidyestimate' a fast, tidy, modern reimagination of
  'ESTIMATE' (2013) <doi:10.1038/ncomms3612>.
	"""
	
	homepage = "https://github.com/KaiAragaki/tidyestimate"
	cran = "tidyestimate" 

	version("1.1.1", md5="24fc6e1fea903356b51c3699d8a36e74")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
