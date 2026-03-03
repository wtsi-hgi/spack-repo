# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactcheckbox(RPackage):
	"""Checkbox Group Input for 'Shiny'

	Provides a checkbox group input for usage in a 'Shiny'
    application. The checkbox group has a head checkbox allowing to check
    or uncheck all the checkboxes in the group. The checkboxes are
    customizable.
	"""
	
	homepage = "https://github.com/stla/reactCheckbox"
	cran = "reactCheckbox" 

	version("1.0.0", md5="d893550975c490b67777de18b80924a5")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
