# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBestree(RPackage):
	"""Branch-Exclusive Splits Trees

	Decision tree algorithm with a major feature added. Allows for users to define an ordering on the partitioning process.
    Resulting in Branch-Exclusive Splits Trees (BEST). Cedric Beaulac and Jeffrey S. Rosentahl (2019) <arXiv:1804.10168>.
	"""
	
	cran = "BESTree" 

	version("0.5.2", md5="22ad55c1b4eac7f986c2ef1a1cc5cdb2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
