# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSudachir(RPackage):
	"""R Interface to 'Sudachi'

	Interface to 'Sudachi' <https://github.com/WorksApplications/Sudachi>,
    a Japanese morphological analyzer. This is a port of what is available in Python.
	"""
	
	homepage = "https://github.com/uribo/sudachir"
	cran = "sudachir" 

	version("0.1.0", md5="4d01d48bd39f3aa4cde6629cac50ada9")

	depends_on("r-cli@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.8:", type=("build", "run"))
	depends_on("r-reticulate@1.17:", type=("build", "run"))
	depends_on("r-tibble@3.0.4:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
