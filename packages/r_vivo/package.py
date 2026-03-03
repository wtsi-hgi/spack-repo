# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVivo(RPackage):
	"""Variable Importance via Oscillations

	Provides an easy to calculate local variable importance measure based on Ceteris Paribus profile 
  and global variable importance measure based on Partial Dependence Profiles.
	"""
	
	homepage = "https://github.com/ModelOriented/vivo"
	cran = "vivo" 

	version("0.2.1", md5="54378045ebb0d06a64312f4d7cdb8230")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
