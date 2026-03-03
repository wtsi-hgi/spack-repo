# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonoinc(RPackage):
	"""Monotonic Increasing

	Various imputation methods are utilized in this package, where one can flag and impute non-monotonic data that is outside of a prespecified range.
	"""
	
	cran = "MonoInc" 

	version("1.1", md5="2a3625b620f5ab28b8e8c30ad9230513")

	depends_on("r-compare", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-sitar", type=("build", "run"))
