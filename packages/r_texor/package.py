# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexor(RPackage):
	"""Converting 'LaTeX' 'R Journal' Articles into 'RJ-web-articles'

	Articles in the 'R Journal' were first authored in 'LaTeX', which performs 
    admirably for 'PDF' files but is less than ideal for modern online interfaces.
    The 'texor' package does all the transitional chores and conversions necessary
    to move to the online versions.
	"""
	
	homepage = "https://github.com/Abhi-1U/texor"
	cran = "texor" 

	version("1.3.0", md5="dfee367f2539bc9aa6f4bfbf3909b961")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-tinytex", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-rjtools", type=("build", "run"))
	depends_on("r-rebib", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("pandoc@3.1:", type=("build", "link", "run"))
