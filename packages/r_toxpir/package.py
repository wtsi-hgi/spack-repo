# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToxpir(RPackage):
	"""Create ToxPi Prioritization Models

	
  Enables users to build 'ToxPi' prioritization models and provides 
  functionality within the grid framework for plotting ToxPi graphs.
  'toxpiR' allows for more customization than the 'ToxPi GUI' 
  (<https://toxpi.org>) and integration into existing workflows for greater 
  ease-of-use, reproducibility, and transparency.
  toxpiR package behaves nearly identically to the GUI; the package 
  documentation includes notes about all differences.
  The vignettes download example files from 
  <https://github.com/ToxPi/ToxPi-example-files>.
	"""
	
	homepage = "https://github.com/ToxPi/toxpiR"
	cran = "toxpiR" 

	version("1.2.1", md5="7b8e323df0ce06c9773fc83592f7eead")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
