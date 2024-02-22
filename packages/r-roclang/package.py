# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoclang(RPackage):
	"""Functions for Diffusing Function Documentations into 'Roxygen'
Comments

	Efficient diffusing of content across function documentations. Sections, parameters or dot parameters are extracted from function documentations and turned into valid Rd character strings, which are ready to diffuse into the 'roxygen' comments of another function by inserting inline code. 
	"""
	
	homepage = "https://github.com/zhuxr11/roclang"
	cran = "roclang" 

	version("0.2.2", md5="62317ae473eccd489381d0b1e8a3e719")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-roxygen2@7.1.1:", type=("build", "run"))
	depends_on("r-rex@1.2:", type=("build", "run"))
