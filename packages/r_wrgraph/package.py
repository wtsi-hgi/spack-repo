# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrgraph(RPackage):
	"""Graphics in the Context of Analyzing High-Throughput Data

	Additional options for making graphics in the context of analyzing high-throughput data are available here.
  This includes automatic segmenting of the current device (eg window) to accommodate multiple new plots, 
  automatic checking for optimal location of legends in plots, small histograms to insert as legends, 
  histograms re-transforming axis labels to linear when plotting log2-transformed data,
  a violin-plot <doi:10.1080/00031305.1998.10480559> function for a wide variety of input-formats, 
  principal components analysis (PCA) <doi:10.1080/14786440109462720> with bag-plots <doi:10.1080/00031305.1999.10474494> to highlight and compare the center areas for groups of samples, 
  generic MA-plots (differential- versus average-value plots) <doi:10.1093/nar/30.4.e15>, 
  staggered count plots and generation of mouse-over interactive html pages.
	"""
	
	cran = "wrGraph" 

	version("1.3.7", md5="c1b4aaeefb372d2b15c9153ab93a57ca")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-wrmisc", type=("build", "run"))
