# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDwdradar(RPackage):
	"""Read Binary Radar Files from 'DWD' (German Weather Service)

	The 'DWD' provides gridded radar data for Germany in binary format. 
  'dwdradar' reads these files and enables a fast conversion into numerical format.
	"""
	
	cran = "dwdradar" 

	version("0.2.10", md5="2f9a0db28f022f754ca6688a64bb59d8")

