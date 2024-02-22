# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadhac(RPackage):
	"""Read Acoustic HAC Format

	Read Acoustic HAC format.
	"""
	
	homepage = "https://github.com/kaskr/HAC"
	cran = "readHAC" 

	version("1.0", md5="13816159d5d19b0d4afda0588cadfd89")

