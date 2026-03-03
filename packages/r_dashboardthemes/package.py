# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDashboardthemes(RPackage):
	"""Customise the Appearance of 'shinydashboard' Applications using
Themes

	Allows manual creation of themes and logos to be used in
    applications created using the 'shinydashboard' package. Removes the need to
    change the underlying css code by wrapping it into a set of convenient R
    functions.
	"""
	
	homepage = "https://github.com/nik01010/dashboardthemes"
	cran = "dashboardthemes" 

	version("1.1.6", md5="0412aef1b3d96fb04a725bfeb02938d2")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-htmltools@0.3.5:", type=("build", "run"))
