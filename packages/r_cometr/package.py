# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCometr(RPackage):
	"""'Comet' API for R

	A convenient 'R' wrapper to the 'Comet' API, which is a cloud
    platform allowing you to track, compare, explain and optimize machine
    learning experiments and models. Experiments can be viewed on the 'Comet'
    online dashboard at <https://www.comet.com>.
	"""
	
	homepage = "https://github.com/comet-ml/cometr"
	cran = "cometr" 

	version("0.4.0", md5="912497d6183968fee4561c570323ddf5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
