# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDivemove(RPackage):
	"""Dive Analysis and Calibration

	Utilities to represent, visualize, filter, analyse, and summarize
	     time-depth recorder (TDR) data.  Miscellaneous functions for
	     handling location data are also provided.
	"""
	
	homepage = "https://github.com/spluque/diveMove"
	cran = "diveMove" 

	version("1.6.2", md5="dc2fcbbc716a659091ce24e8bd89bf9d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-unireg", type=("build", "run"))
