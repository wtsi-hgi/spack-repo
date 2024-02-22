# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFillr(RPackage):
	"""Fill Missing Values in Vectors

	Edit vectors to fill missing values, based on the vector itself.
	"""
	
	homepage = "https://jelger12.github.io/fillr/"
	cran = "fillr" 

	version("1.0.0", md5="c2322d431a9c8dbe28a7ea493592b049")

