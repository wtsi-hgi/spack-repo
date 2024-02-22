# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REndoswitch(RPackage):
	"""Endogenous Switching Regression Models

	Maximum likelihood estimation of endogenous switching regression models from Heckman (1979) <doi:10.2307/1912352> and estimation of treatment effects.  
	"""
	
	homepage = "https://github.com/cbw1243/endoSwitch"
	cran = "endoSwitch" 

	version("1.0.0", md5="3462320a4dcd333ab94af83479943a0b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-maxlik@1.3.6:", type=("build", "run"))
	depends_on("r-msm@1.6.7:", type=("build", "run"))
