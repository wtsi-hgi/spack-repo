# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActogrammr(RPackage):
	"""Read in Activity Data and Plot Actograms

	Read in activity measurements from standard file formats
  used by circadian rhythm researchers, currently only 'ClockLab' format,
  and process and plot the data.  The central type of plot is the actogram,
  as first described by in "Activity and distribution of certain wild mice 
  in relation to biotic communities" by MS Johnson (1926) <doi:10.2307/1373575>.
	"""
	
	cran = "actogrammr" 

	version("0.2.3", md5="d1337175c187e877396aaab3d69931cc")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
