# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumform(RPackage):
	"""Tools to Format Numbers for Publication

	Format numbers and plots for publication; includes the removal of leading zeros,
           standardization of number of digits, addition of affixes, and a p-value formatter. These
           tools combine the functionality of several 'base' functions such as 'paste()',
           'format()', and 'sprintf()' into specific use case functions that are named in a way
           that is consistent with usage, making their names easy to remember and easy to deploy.
	"""
	
	homepage = "https://github.com/trinker/numform"
	cran = "numform" 

	version("0.7.0", md5="517b28237005593db16e04e81c95821e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
