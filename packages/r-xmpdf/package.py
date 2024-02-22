# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXmpdf(RPackage):
	"""Edit 'XMP' Metadata and 'PDF' Bookmarks and Documentation Info

	Edit 'XMP' metadata <https://en.wikipedia.org/wiki/Extensible_Metadata_Platform> 
    in a variety of media file formats as well as 
    edit bookmarks (aka outline aka table of contents) and documentation info entries in 'pdf' files.
    Can detect and use a variety of command-line tools to perform these operations such as
    'exiftool' <https://exiftool.org/>, 'ghostscript' <https://www.ghostscript.com/>, 
    and/or 'pdftk' <https://gitlab.com/pdftk-java/pdftk>.
	"""
	
	homepage = "https://trevorldavis.com/R/xmpdf/dev/"
	cran = "xmpdf" 

	version("0.1.4", md5="34905d3d997b80ee389404b65fdd6947")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-datetimeoffset@0.2.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("ghostscript", type=("build", "link", "run"))
	depends_on("exiv2", type=("build", "link", "run"))
