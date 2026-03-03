# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetip(RPackage):
	"""'IP' Address 'Lookup'

	A micro-package for getting your 'IP' address, either the 
    local/internal or the public/external one. Currently only 'IPv4' addresses
    are supported.
	"""
	
	cran = "getip" 

	version("0.1-4", md5="d366e65b64a5429bacadf8fcc0081bcf")

	depends_on("r@3:", type=("build", "run"))
