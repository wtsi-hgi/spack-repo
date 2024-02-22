# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInstallLoad(RPackage):
	"""Check, Install and Load CRAN Packages

	The function 'install_load' checks the local R library(ies) to see
    if the required package(s) is/are installed or not. If the package(s)
    is/are not installed, then the package(s) will be installed along with
    the required dependency(ies). This function pulls source or
    binary packages from the Posit/RStudio-sponsored CRAN mirror. Lastly, the
    chosen package(s) is/are loaded. The function 'load_package' simply loads
    the provided package(s). If this package does not fit your needs, then you
    may want to consider these other R packages: 'needs', 'easypackages',
    'pacman', 'pak', 'anyLib', and/or 'librarian'.
	"""
	
	homepage = "https://gitlab.com/iembry/install.load"
	cran = "install.load" 

	version("1.2.5", md5="cfe2d9a9eec07818b13ab973b2d2d8bf")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
