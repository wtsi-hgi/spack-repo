# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLimmagui(RPackage):
	"""GUI for limma Package With Two Color Microarrays

	A Graphical User Interface for differential expression analysis of two-color microarray data using the limma package.
	"""
	
	homepage = "http://bioinf.wehi.edu.au/limmaGUI/"
	bioc = "limmaGUI"

	version("1.84.0", commit="0b791cd628035470acf1e3e701f432ae9cb71498")
	version("1.78.0", commit="76731c44df19fee093d55939cd599cf412618d5f")

	depends_on("r-limma", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
