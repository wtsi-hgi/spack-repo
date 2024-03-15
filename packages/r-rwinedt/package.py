# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwinedt(RPackage):
	"""R Interface to 'WinEdt'

	A plug in for using 'WinEdt' as an editor for R.
	"""
	
	homepage = "http://www.winedt.com/"
	cran = "RWinEdt" 

	version("2.0-6", md5="40da86418e8f89404bed7f4bb2a0691c")

	depends_on("r@2.11:", type=("build", "run"))
