# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocLogs(RPackage):
	"""BioConductor Package Downloads Stats

	Download stats reported from the BioConductor.org stats website.
	"""
	
	homepage = "https://github.com/mponce0/bioC.logs"
	cran = "bioC.logs" 

	version("1.2.1", md5="0966d6c1960f03af1806552945ed1775")

