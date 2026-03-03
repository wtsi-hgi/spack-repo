# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLar(RPackage):
	"""History of labour relations package

	This package is intended for researchers studying historical labour relations (see http://www.historyoflabourrelations.org). The package allows for easy access of excel files in the standard defined by the Global Collaboratory on the History of Labour Relations. The package also allows for visualisation of labour relations according to the Collaboratory's format.
	"""
	
	cran = "lar" 

	version("0.1-2", md5="9facda662f03f4f4eefb35fb8c1f3631")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-treemap", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
