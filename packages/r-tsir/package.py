# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsir(RPackage):
	"""An Implementation of the TSIR Model

	An implementation of the time-series Susceptible-Infected-Recovered (TSIR) model using a number of different fitting options for infectious disease time series data. The manuscript based on this package can be found here <doi:10.1371/journal.pone.0185528>. The method implemented here is described by Finkenstadt and Grenfell (2000) <doi:10.1111/1467-9876.00187>.
	"""
	
	cran = "tsiR" 

	version("0.4.3", md5="b87be29f60981ced6d15883aec435c00")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
