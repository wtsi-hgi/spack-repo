# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConditionz(RPackage):
	"""Control How Many Times Conditions are Thrown

	Provides ability to control how many times in function
    calls conditions are thrown (shown to the user). Includes control of
    warnings and messages.
	"""
	
	homepage = "https://github.com/ropenscilabs/conditionz"
	cran = "conditionz" 

	version("0.1.0", md5="f1b355e36abdb38c33950b6d029e578d")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
