# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextclean(RPackage):
	"""Text Cleaning Tools

	Tools to clean and process text.  Tools are geared at checking for substrings that
          are not optimal for analysis and replacing or removing them (normalizing) with more
          analysis friendly substrings (see Sproat, Black, Chen, Kumar, Ostendorf, & Richards
          (2001) <doi:10.1006/csla.2001.0169>) or extracting them into new variables. For
          example, emoticons are often used in text but not always easily handled by analysis
          algorithms.  The replace_emoticon() function replaces emoticons with word
          equivalents.
	"""
	
	homepage = "https://github.com/trinker/textclean"
	cran = "textclean" 

	version("0.9.3", md5="f0e1824c419bac6a53be1445e4eb34fb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-english@1.0.2:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-lexicon@1:", type=("build", "run"))
	depends_on("r-mgsub@1.5:", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-textshape@1.0.1:", type=("build", "run"))
