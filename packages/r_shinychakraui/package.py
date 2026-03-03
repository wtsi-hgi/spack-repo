# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinychakraui(RPackage):
	"""A Wrapper of the 'React' Library 'Chakra UI' for 'Shiny'

	Makes the 'React' library 'Chakra UI' usable in 'Shiny' apps. 'Chakra UI' components include alert dialogs, drawers (sliding panels), menus, modals, popovers, sliders, and more. 
	"""
	
	homepage = "https://github.com/stla/shinyChakraUI"
	cran = "shinyChakraUI" 

	version("1.1.1", md5="00c70909b80ab3cac55cef729f3d6036")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))
