# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdcard(RPackage):
	"""Update Chinese ID Card Number to Eighteen Digits

	The digits of the old version (before 2000 year) of 'Chinese ID Card Number' is 15, this package aims to update to the current version of 18 digits. Besides, this package can help check whether the given 'ID' is right or not.
	"""
	
	cran = "IDCard" 

	version("0.3.0", md5="47c6bba288062dbf2eed13ec24fc74ea")

	depends_on("r-stringr", type=("build", "run"))
