# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoah(RPackage):
	"""Create Unique Pseudonymous Animal Names

	Generate pseudonymous animal names that are delightful and easy to 
    remember like the Likable Leech and the Proud Chickadee. A unique pseudonym 
    can be created for every unique element in a vector or row in a data frame. 
    Pseudonyms can be customized and tracked over time, so that the same input 
    is always assigned the same pseudonym.
	"""
	
	homepage = "https://github.com/Teebusch/noah"
	cran = "noah" 

	version("0.1.0", md5="8a6ae9a8abadde3868a0b249d9c4acfc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
