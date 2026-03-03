# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBabynamesil(RPackage):
	"""Israel Baby Names 1948-2022

	Israeli baby names provided by Israel's Central Bureau of Statistics. The package contains only names used for at least 5 children in at least one gender and sector ("Jewish", "Muslim", "Christian", "Druze" and "Other"). Data was downloaded from: <https://www.cbs.gov.il/he/publications/LochutTlushim/2020/%D7%A9%D7%9E%D7%95%D7%AA-%D7%A4%D7%A8%D7%98%D7%99%D7%99%D7%9D.xlsx>.
	"""
	
	homepage = "https://github.com/aviezerl/babynamesIL"
	cran = "babynamesIL" 

	version("0.0.2", md5="b9faf27d645742cd27bfc9a8bf568874")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
