# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecords(RPackage):
	"""Record Values and Record Times

	Functions for generating k-record values and k-record
        times
	"""
	
	cran = "Records" 

	version("1.0", md5="fab26b8f99b1c97bccf9aebfc91ad3fe")

