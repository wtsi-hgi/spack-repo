# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsleep(RPackage):
	"""Analysis of Sleep Data

	A toolbox for sleep data processing, visualization and analysis. Tools for state of the art automatic sleep stages scoring.
	"""
	
	homepage = "https://rsleep.org/"
	cran = "rsleep" 

	version("1.0.12", md5="8f1dcfe7f29748b17f8c080185243895")

	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edfreader", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-psd", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
