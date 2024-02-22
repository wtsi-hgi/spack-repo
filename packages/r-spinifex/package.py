# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpinifex(RPackage):
	"""Manual Tours, Manual Control of Dynamic Projections of Numeric
Multivariate Data

	Data visualization tours animates linear projection 
  of multivariate data as its basis (ie. orientation) changes. The 'spinifex' 
  packages generates paths for manual tours by manipulating the contribution of 
  a single variable at a time Cook & Buja (1997) 
  <doi:10.1080/10618600.1997.10474754>. Other types of tours, such as grand 
  (random walk) and guided (optimizing some objective function) are available 
  in the 'tourr' package Wickham et al. <doi:10.18637/jss.v040.i02>. 
  'spinifex' builds on 'tourr' and can render tours with 'gganimate' and 
  'plotly' graphics, and allows for exporting as an .html widget and as an .gif, 
  respectively. This work is fully discussed in Spyrison & Cook (2020) 
  <doi:10.32614/RJ-2020-027>.
	"""
	
	homepage = "https://github.com/nspyrison/spinifex/"
	cran = "spinifex" 

	version("0.3.7.0", md5="ca09493c7fa8ddef135e0d731a2209b3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tourr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rdimtools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
