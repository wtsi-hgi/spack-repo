# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwitchboard(RPackage):
	"""An Agile Widget Engine for Real-Time, Dynamic Visualizations

	An unsorted collection of visualization widgets rendered in 'Tcl/Tk'<https://www.tcl.tk/> to generate agile dashboards for your iterative simulations. Widgets include progress bars, counters, eavesdroppers, injectors, switches, and sliders for dynamic manipulation and visualization of simulation parameters.
	"""
	
	homepage = "http://lajeunesse.myweb.usf.edu/"
	cran = "switchboard" 

	version("0.1", md5="9e9900504ab2af7ab22faddb078aecd9")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("tcl", type=("build", "link", "run"))
	depends_on("tk", type=("build", "link", "run"))
