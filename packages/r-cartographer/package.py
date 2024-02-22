# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCartographer(RPackage):
	"""Turn Place Names into Map Data

	A tool for easily matching spatial data when you have a list of
    place/region names. You might have a data frame that came from a
    spreadsheet tracking some data by suburb or state. This package can
    convert it into a spatial data frame ready for plotting. The actual map
    data is provided by other packages (or your own code).
	"""
	
	homepage = "https://github.com/cidm-ph/cartographer"
	cran = "cartographer" 

	version("0.2.1", md5="06dfab343f0917c294f5f1f588a60890")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-sf@1.0.12:", type=("build", "run"))
