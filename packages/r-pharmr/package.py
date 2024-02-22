# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPharmr(RPackage):
	"""Interface to the 'Pharmpy' 'Pharmacometrics' Library

	Interface to the 'Pharmpy' 'pharmacometrics' library. The 'Reticulate' package is used to interface Python from R.
	"""
	
	homepage = "https://github.com/pharmpy/pharmr"
	cran = "pharmr" 

	version("0.96.0", md5="35d08ef34c84b22fb2fb599537dd4681")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-altair@4:", type=("build", "run"))
	depends_on("r-reticulate@1.19:", type=("build", "run"))
	depends_on("python@3.9.0:", type=("build", "link", "run"))
