# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSentimentr(RPackage):
	"""Calculate Text Polarity Sentiment

	Calculate text polarity sentiment at the sentence level and
         optionally aggregate by rows or grouping variable(s).
	"""
	
	homepage = "https://github.com/trinker/sentimentr"
	cran = "sentimentr" 

	version("2.9.0", md5="acda9b6ce6c6848dc40c0e3286efc092")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lexicon@1.2.1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-syuzhet", type=("build", "run"))
	depends_on("r-textclean@0.6.1:", type=("build", "run"))
	depends_on("r-textshape@1.3:", type=("build", "run"))
