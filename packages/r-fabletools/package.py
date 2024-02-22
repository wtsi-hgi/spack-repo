# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabletools(RPackage):
	"""Core Tools for Packages in the 'fable' Framework

	Provides tools, helpers and data structures for
    developing models and time series functions for 'fable' and extension
    packages. These tools support a consistent and tidy interface for time
    series modelling and analysis.
	"""
	
	homepage = "https://fabletools.tidyverts.org/"
	cran = "fabletools" 

	version("0.4.0", md5="ffceb4f3432bc347d384e96fd6027644")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-tsibble@0.9:", type=("build", "run"))
	depends_on("r-tibble@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-vctrs@0.2.2:", type=("build", "run"))
	depends_on("r-distributional@0.3.0.9000:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
