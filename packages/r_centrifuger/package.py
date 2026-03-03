# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCentrifuger(RPackage):
	"""Non-Trivial Balance of Centrifuge Rotors

	Find the numbers of test tubes that can be balanced in centrifuge
    rotors and show various ways to load them. Refer to Pham (2020)
    <doi:10.31224/osf.io/4xs38> for more information on package functionality.
	"""
	
	homepage = "https://phamdn.shinyapps.io/centrifugeR/"
	cran = "centrifugeR" 

	version("0.1.7", md5="1f78d8ab154e1785e489867f54f351be")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-pracma@2.4.2:", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-shinythemes@1.2:", type=("build", "run"))
