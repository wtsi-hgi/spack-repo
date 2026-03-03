# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowdr(RPackage):
	"""Full Pattern Summation of X-Ray Powder Diffraction Data

	Full pattern summation of X-ray powder diffraction data as
  described in Chipera and Bish (2002) <doi:10.1107/S0021889802017405> and
  Butler and Hillier (2021) <doi:10.1016/j.cageo.2020.104662>.
  Derives quantitative estimates of crystalline and amorphous phase
  concentrations in complex mixtures.
	"""
	
	homepage = "https://github.com/benmbutler/powdR"
	cran = "powdR" 

	version("1.3.0", md5="9257bea82d856e2252c8ecf52d5670bb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-reshape@0.8.8:", type=("build", "run"))
	depends_on("r-plotly@4.9.2.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggpubr@0.2.5:", type=("build", "run"))
	depends_on("r-shiny@1.4.0.2:", type=("build", "run"))
	depends_on("r-dt@0.13:", type=("build", "run"))
	depends_on("r-nnls@1.4:", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.1:", type=("build", "run"))
	depends_on("r-baseline@1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-factominer@2.3:", type=("build", "run"))
	depends_on("r-factoextra@1.0.7:", type=("build", "run"))
	depends_on("r-rxylib@0.2.6:", type=("build", "run"))
