# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsurer(RPackage):
	"""Ensure Values at Runtime

	Add simple runtime contracts to R values. These ensure that values
    fulfil certain conditions and will raise appropriate errors if they do not.
	"""
	
	homepage = "https://github.com/smbache/ensurer"
	cran = "ensurer" 

	version("1.1", md5="0f3ea28ed5b5276143f126737fb116fa")

