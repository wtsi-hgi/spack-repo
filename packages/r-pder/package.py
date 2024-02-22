# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPder(RPackage):
	"""Panel Data Econometrics with R

	Data sets for the Panel Data Econometrics with R <doi:10.1002/9781119504641> book.
	"""
	
	homepage = "https://cran.r-project.org/package=pder"
	cran = "pder" 

	version("1.0-2", md5="c958ef9dfb057bfce1ce3338b40ae3a2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
