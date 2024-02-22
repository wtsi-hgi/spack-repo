# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2dictionary(RPackage):
	"""A Mini-Dictionary for 'R', 'Shiny' and 'Rmarkdown' Documents

	Despite the predominant use of R for data manipulation and various robust statistical calculations, in recent years, more people from various disciplines are beginning to use R for other purposes. A critical milestone that has enabled large influx of users in the R community is the development of the Tidyverse family of packages and Rmarkdown. With the latter, one can write all kinds of documents and produce output in formats such html and pdf very easily. In doing this seemlessly, further tools are needed for such users to easily and freely write in R for all kinds of purposes. The r2dictionary introduces a means for users to directly search for definitions of terms within the R environment.
	"""
	
	homepage = "https://r2dictionary.obi.obianom.com"
	cran = "r2dictionary" 

	version("0.2", md5="248375d3054e3ab7ea49c75f80f7c0e3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
