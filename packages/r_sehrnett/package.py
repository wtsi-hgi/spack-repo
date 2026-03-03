# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSehrnett(RPackage):
	"""A Very Nice Interface to 'WordNet'

	A very nice interface to Princeton's 'WordNet' without 'rJava' dependency. 'WordNet' data is not included. Princeton University makes 'WordNet' available to research and commercial users free of charge provided the terms of their license (<https://wordnet.princeton.edu/license-and-commercial-use>) are followed, and proper reference is made to the project using an appropriate citation (<https://wordnet.princeton.edu/citing-wordnet>).
	"""
	
	homepage = "https://github.com/chainsawriot/sehrnett"
	cran = "sehrnett" 

	version("0.1.0", md5="50f8478490d07754532286a4365d72aa")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
