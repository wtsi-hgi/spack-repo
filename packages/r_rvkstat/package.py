# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvkstat(RPackage):
	"""R Interface to API 'vk.com'

	Load data from vk.com api about your communiti users and views,
    ads performance, post on user wall and etc.	For more information 
    see API Documentation <https://vk.com/dev/first_guide>.
	"""
	
	homepage = "https://selesnow.github.io/rvkstat/"
	cran = "rvkstat" 

	version("3.2.0", md5="3d7c5d2094e3dedeb84451b562570b30")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
