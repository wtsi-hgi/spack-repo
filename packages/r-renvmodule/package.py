# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRenvmodule(RPackage):
	"""Interface to Allow Full Use of the Environment Modules System
for Unix

	Provides environment modules functionality, which enables use of the Environment Modules system (<http://modules.sourceforge.net/>) from within the R environment. By default the user's login shell environment (ie. "bash -l") will be used to initialize the current session. The module function can also; load or unload specific software, list all the loaded software within the current session, and list all the applications available for loading from the module system. Lastly, the module function can remove all loaded software from the current session.
	"""
	
	cran = "RenvModule" 

	version("1.1", md5="d4914815b90d379595ce624ae4850343")

