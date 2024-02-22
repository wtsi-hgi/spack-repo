# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyTailwind(RPackage):
	"""'TailwindCSS' for Shiny Apps

	Allows 'TailwindCSS' to be used in Shiny apps with just-in-time 
  compiling, custom css with '@apply' directive, and custom tailwind 
  configurations.
	"""
	
	homepage = "https://github.com/kylebutts/shiny.tailwind"
	cran = "shiny.tailwind" 

	version("0.2.2", md5="9a350ec2c88d11230cb995e95296ff5d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
