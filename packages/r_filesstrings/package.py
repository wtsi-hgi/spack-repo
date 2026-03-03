# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilesstrings(RPackage):
	"""Handy File and String Manipulation

	This started out as a package for file and string
    manipulation.  Since then, the 'fs' and 'strex' packages emerged,
    offering functionality previously given by this package (but it's done
    better in these new ones).  Those packages have hence almost pushed
    'filesstrings' into extinction.  However, it still has a small number
    of unique, handy file manipulation functions which can be seen in the
    vignette.  One example is a function to remove spaces from all file
    names in a directory.
	"""
	
	homepage = "https://rorynolan.github.io/filesstrings/"
	cran = "filesstrings" 

	version("3.4.0", md5="40a68c21f47b7994cc9bc19f8bb6b548")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-checkmate@1.9.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.3.3:", type=("build", "run"))
	depends_on("r-strex@1.6:", type=("build", "run"))
	depends_on("r-stringi@1.7.8:", type=("build", "run"))
	depends_on("r-withr@2.1:", type=("build", "run"))
