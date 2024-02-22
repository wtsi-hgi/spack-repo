# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaijr(RPackage):
	"""Operations to Ease Data Analyses Specific to Nigeria

	A set of convenience functions as well as geographical/political
  data about Nigeria, aimed at simplifying work with data and information that
  are specific to the country.
	"""
	
	homepage = "https://brovic.github.io/naijR/"
	cran = "naijR" 

	version("0.6.0", md5="e5f919af8ca90bb6bcf13e7bde194f55")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-mapdata@2.3:", type=("build", "run"))
	depends_on("r-maps@3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-sf@1.0.13:", type=("build", "run"))
	depends_on("r-stringi@1.7.6:", type=("build", "run"))
