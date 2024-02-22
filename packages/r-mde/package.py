# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMde(RPackage):
	"""Missing Data Explorer

	Correct identification and handling of missing data is one of the most important steps in any analysis. To aid this process, 'mde' provides a very easy to use yet robust framework to quickly get an idea of where the missing data
             lies and therefore find the most appropriate action to take.
             Graham WJ (2009) <doi:10.1146/annurev.psych.58.110405.085530>. 
	"""
	
	homepage = "https://github.com/Nelson-Gon/mde"
	cran = "mde" 

	version("0.3.2", md5="4501d3835c12188a383972ec16af971d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.0.3:", type=("build", "run"))
