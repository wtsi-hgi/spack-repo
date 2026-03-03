# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsciicast(RPackage):
	"""Create 'Ascii' Screen Casts from R Scripts

	Record 'asciicast' screen casts from R scripts. Convert them
    to animated SVG images, to be used in 'README' files, or blog posts.
    Includes 'asciinema-player' as an 'HTML' widget, and an 'asciicast'
    'knitr' engine, to embed 'ascii' screen casts in 'Rmarkdown'
    documents.
	"""
	
	homepage = "https://asciicast.r-lib.org/"
	cran = "asciicast" 

	version("2.3.1", md5="578583bc17279b6a9b29fa8901f5849c")

	depends_on("r-cli@3.3.0.9000:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magick@2.2.9002:", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zliba", type=("build", "link", "run"))
	depends_on("icu4c", type=("build", "link", "run"))
	depends_on("libiconv", type=("build", "link", "run"))
