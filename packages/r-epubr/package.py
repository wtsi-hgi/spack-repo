# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpubr(RPackage):
	"""Read EPUB File Metadata and Text

	Provides functions supporting the reading and parsing of internal e-book content from EPUB files. 
    The 'epubr' package provides functions supporting the reading and parsing of internal e-book content from EPUB files. 
    E-book metadata and text content are parsed separately and joined together in a tidy, nested tibble data frame. 
    E-book formatting is not completely standardized across all literature. 
    It can be challenging to curate parsed e-book content across an arbitrary collection of e-books 
    perfectly and in completely general form, to yield a singular, consistently formatted output. 
    Many EPUB files do not even contain all the same pieces of information in their respective metadata. 
    EPUB file parsing functionality in this package is intended for relatively general application to arbitrary EPUB e-books. 
    However, poorly formatted e-books or e-books with highly uncommon formatting may not work with this package. 
    There may even be cases where an EPUB file has DRM or some other property that makes it impossible to read with 'epubr'. 
    Text is read 'as is' for the most part. The only nominal changes are minor substitutions, for example curly quotes changed to straight quotes. 
    Substantive changes are expected to be performed subsequently by the user as part of their text analysis. 
    Additional text cleaning can be performed at the user's discretion, such as with functions from packages like 'tm' or 'qdap'.
	"""
	
	homepage = "https://docs.ropensci.org/epubr/"
	cran = "epubr" 

	version("0.6.4", md5="d37d1a8c717cdada30b01b25d0054af4")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xslt", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
