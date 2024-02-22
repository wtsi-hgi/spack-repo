# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBupaverse(RPackage):
	"""Easily Install and Load the 'bupaverse'

	The 'bupaverse' is an open-source, integrated suite of R-packages for handling and analysing business process data,
    developed by the Business Informatics research group at Hasselt University, Belgium. Profoundly inspired by the 'tidyverse' package,
    the 'bupaverse' package is designed to facilitate the installation and loading of multiple 'bupaverse' packages in a single step.
    Learn more about 'bupaverse' at the <https://bupar.net> homepage.
	"""
	
	homepage = "https://bupar.net/"
	cran = "bupaverse" 

	version("0.1.0", md5="fb857ef24024872fe8500c6e24aa9d3a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bupar@0.5.1:", type=("build", "run"))
	depends_on("r-edear@0.9.1:", type=("build", "run"))
	depends_on("r-eventdatar@0.3.1:", type=("build", "run"))
	depends_on("r-processcheckr@0.1.4:", type=("build", "run"))
	depends_on("r-processmapr@0.5.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-glue@1:", type=("build", "run"))
