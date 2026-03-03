# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlrx(RPackage):
	"""Setup, Run and Analyze 'NetLogo' Model Simulations from 'R' via
'XML'

	Setup, run and analyze 'NetLogo' (<https://ccl.northwestern.edu/netlogo/>) model simulations in 'R'.
    'nlrx' experiments use a similar structure as 'NetLogos' Behavior Space experiments. 
    However, 'nlrx' offers more flexibility and additional tools for running and analyzing complex simulation designs and sensitivity analyses.
    The user defines all information that is needed in an intuitive framework, using class objects.
    Experiments are submitted from 'R' to 'NetLogo' via 'XML' files that are dynamically written, based on specifications defined by the user.
    By nesting model calls in future environments, large simulation design with many runs can be executed in parallel.
    This also enables simulating 'NetLogo' experiments on remote high performance computing machines.
    In order to use this package, 'Java' and 'NetLogo' (>= 5.3.1) need to be available on the executing system.
	"""
	
	homepage = "https://docs.ropensci.org/nlrx/"
	cran = "nlrx" 

	version("0.4.5", md5="53ae6be4bf217d481d11cffec9d813f5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-sensitivity", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-easyabc", type=("build", "run"))
	depends_on("openjdk@11:", type=("build", "link", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
	depends_on("openssl", type=("build", "link", "run"))
	depends_on("udunits@2:", type=("build", "link", "run"))
	depends_on("proj@4:", type=("build", "link", "run"))
	depends_on("geos", type=("build", "link", "run"))
	depends_on("gdal", type=("build", "link", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
