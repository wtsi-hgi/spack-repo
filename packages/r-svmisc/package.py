# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RSvmisc(RPackage):
	"""'SciViews' - Miscellaneous Functions

	Miscellaneous functions for 'SciViews' or general use: manage a
  temporary environment attached to the search path for temporary variables you
  do not want to save() or load(), test if 'Aqua', 'Mac', 'Win', ... Show
  progress bar, etc.
	"""
	
	homepage = "https://github.com/SciViews/svMisc"
	cran = "svMisc" 

	version("1.2.3", md5="b94227b8913984ed493eefca71c45975")

	depends_on("r@2.13.0:", type=("build", "run"))
