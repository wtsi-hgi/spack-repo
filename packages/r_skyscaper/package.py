# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkyscaper(RPackage):
	"""Data Analysis and Visualization for Skyscape Archaeology

	Data reduction, visualization and statistical analysis of measurements of orientation of archaeological structures, following Silva (2020) <doi:10.1016/j.jas.2020.105138>.
	"""
	
	cran = "skyscapeR" 

	version("1.0.0", md5="e80f62c893e4519a229d1bec62ce4da9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-swephr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-oce", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
