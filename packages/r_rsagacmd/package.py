# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsagacmd(RPackage):
	"""Linking R with the Open-Source 'SAGA-GIS' Software

	Provides an R scripting interface to the open-source 'SAGA-GIS' 
    (System for Automated Geoscientific Analyses Geographical Information
    System) software. 'Rsagacmd' dynamically generates R functions for every
    'SAGA-GIS' geoprocessing tool based on the user's currently installed
    'SAGA-GIS' version. These functions are contained within an S3 object
    and are accessed as a named list of libraries and tools. This structure
    facilitates an easier scripting experience by organizing the large number
    of 'SAGA-GIS' geoprocessing tools (>700) by their respective library.
    Interactive scripting can fully take advantage of code autocompletion tools
    (e.g. in 'Rstudio'), allowing for each tools syntax to be quickly
    recognized. Furthermore, the most common types of spatial data (via the
    'terra', 'sp', and 'sf' packages) along with non-spatial data are
    automatically passed from R to the 'SAGA-GIS' command line tool for
    geoprocessing operations, and the results are loaded as the appropriate R
    object. Outputs from individual 'SAGA-GIS' tools can also be chained using
    pipes from the 'magrittr' and 'dplyr' packages to combine complex
    geoprocessing operations together in a single statement. 'SAGA-GIS' is
    available under a GPLv2 / LGPLv2 licence from
    <https://sourceforge.net/projects/saga-gis/> including Windows x86/x64
    and macOS binaries. SAGA-GIS is also included in Debian/Ubuntu default software
    repositories. Rsagacmd has currently been tested on 'SAGA-GIS' versions
    from 2.3.1 to 9.2 on Windows, Linux and macOS.
	"""
	
	homepage = "https://stevenpawley.github.io/Rsagacmd/"
	cran = "Rsagacmd" 

	version("0.4.2", md5="11386222653ef1dc71afc25bb14170ea")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra@1.7:", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("saga-gis@2.3.1:", type=("build", "link", "run"))
