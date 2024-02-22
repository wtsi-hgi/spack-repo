# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVersions(RPackage):
	"""Query and Install Specific Versions of Packages on CRAN

	Installs specified versions of R packages hosted on CRAN and
    provides functions to list available versions and the versions of currently
    installed packages. These tools can be used to help make R projects and
    packages more reproducible. 'versions' fits in the narrow gap between
    the 'devtools' install_version() function and the 'checkpoint' package.
    devtools::install_version() installs a stated package version from source files
    stored on the CRAN archives. However CRAN does not store binary versions of
    packages so Windows users need to have RTools installed and Windows and OSX
    users get longer installation times. 'checkpoint' uses the Revolution Analytics
    MRAN server to install packages (from source or binary) as they were available
    on a given date. It also provides a helpful interface to detect the packages
    in use in a directory and install all of those packages for a given date.
    'checkpoint' doesn't provide install.packages-like functionality however, and
    that's what 'versions' aims to do, by querying MRAN. As MRAN only goes back to
    2014-09-17, 'versions' can't install packages archived before this date.
	"""
	
	cran = "versions" 

	version("0.3", md5="193eaf2acf06798e4a4e5fa8e38d60a1")

