# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhcnuggetsr(RPackage):
	"""Call MHCnuggets

	
    MHCnuggets (<https://github.com/KarchinLab/mhcnuggets>) is a Python
    tool to predict MHC class I and MHC class II epitopes.
    This package allows one to call MHCnuggets from R.
	"""
	
	homepage = "https://github.com/richelbilderbeek/mhcnuggetsr/"
	cran = "mhcnuggetsr" 

	version("1.1", md5="4d36ac84a8ec7337743f963eaae06390")

	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
