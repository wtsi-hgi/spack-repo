# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynparam(RPackage):
	"""Creating Meta-Information for Parameters

	Provides tools for describing parameters of algorithms in an abstract way.
  Description can include an id, a description, a domain (range or list of values),
  and a default value. 'dynparam' can also convert parameter sets to a 'ParamHelpers' format, 
  in order to be able to use 'dynparam' in conjunction with 'mlrMBO'.
	"""
	
	homepage = "https://github.com/dynverse/dynparam"
	cran = "dynparam" 

	version("1.0.2", md5="0f384139bf868c3b33b125ef0018e947")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-carrier", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dynutils@1.0.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
