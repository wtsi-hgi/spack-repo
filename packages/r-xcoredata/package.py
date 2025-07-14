# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXcoredata(RPackage):
	"""data package for xcore

	Provides data to use with xcore package.
	"""
	
	bioc = "xcoredata"

	version("1.12.0", commit="6e7544b2bc93f20ae5300246686b173ac63eae71")
	version("1.6.0", commit="2c32bd1d7e0edf455bd9b029b8df8e84726a36ad")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-experimenthub@2.2:", type=("build", "run"))

