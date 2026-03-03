# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCredule(RPackage):
	"""Credit Default Swap Functions

	It provides functions to bootstrap Credit Curves from market quotes (Credit Default Swap - CDS - spreads) and price Credit Default Swaps - CDS.
	"""
	
	homepage = "https://github.com/blenezet/credule"
	cran = "credule" 

	version("0.1.4", md5="fefc5bf03fde1fe0a53bb8ee23b60c2c")

	depends_on("r@2.14.1:", type=("build", "run"))
