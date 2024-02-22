# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutodeskr(RPackage):
	"""An Interface to the 'AutoDesk' 'API' Platform

	An interface to the 'AutoDesk' 'API' Platform including the Authentication 
    'API' for obtaining authentication to the 'AutoDesk' Forge Platform, Data Management 
    'API' for managing data across the platform's cloud services, Design Automation 'API'
    for performing automated tasks on design files in the cloud, Model
    Derivative 'API' for translating design files into different formats, sending
    them to the viewer app, and extracting design data, and Viewer for rendering
    2D and 3D models (see <https://developer.autodesk.com> for more information).
	"""
	
	homepage = "https://github.com/paulgovan/autodeskr"
	cran = "AutoDeskR" 

	version("0.1.3", md5="a9cbcc0d1f68bd3962a7382b851d915d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
