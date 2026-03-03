# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopchef(RPackage):
	"""Top Chef Data

	Several datasets which describe the chef contestants in Top Chef, 
    the challenges that they compete in, and the results of those challenges. 
    This data is useful for practicing data wrangling, graphing, and analyzing 
    how each season of Top Chef played out.
	"""
	
	homepage = "https://github.com/celevitz/topChef"
	cran = "topChef" 

	version("0.1.0", md5="25e8eff83d1b97d4e7e6a833cf763c70")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
