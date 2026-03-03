# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyuzhet(RPackage):
	"""Extracts Sentiment and Sentiment-Derived Plot Arcs from Text

	Extracts sentiment and sentiment-derived plot arcs
    from text using a variety of sentiment dictionaries conveniently
    packaged for consumption by R users.  Implemented dictionaries include
    "syuzhet" (default) developed in the Nebraska Literary Lab
    "afinn" developed by Finn Årup Nielsen, "bing" developed by Minqing Hu
    and Bing Liu, and "nrc" developed by Mohammad, Saif M. and Turney, Peter D.
    Applicable references are available in README.md and in the documentation
    for the "get_sentiment" function.  The package also provides a hack for
    implementing Stanford's coreNLP sentiment parser. The package provides
    several methods for plot arc normalization.
	"""
	
	homepage = "https://github.com/mjockers/syuzhet"
	cran = "syuzhet" 

	version("1.0.7", md5="a5542d4e88fdfd5053714dd0986a1b4d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-textshape@1.3:", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-dtt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
