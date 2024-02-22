# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapidxmlr(RPackage):
	"""'Rapidxml' C++ Header Files

	Provides XML parsing capability through the 'Rapidxml' 'C++' header-only library.
	"""
	
	cran = "rapidxmlr" 

	version("0.1.0", md5="9081794bb4717d45e764851bed70d21f")

