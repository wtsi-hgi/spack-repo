# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRyacas0(RPackage):
	"""Legacy 'Ryacas' (Interface to 'Yacas' Computer Algebra System)

	A legacy version of 'Ryacas', an interface to the 'yacas' computer algebra system (<http://www.yacas.org/>).
	"""
	
	homepage = "https://github.com/r-cas/ryacas0"
	cran = "Ryacas0" 

	version("0.4.4", md5="f0e7e2b115ceefe6494c036cf661f5f7", url="https://cran.r-project.org/src/contrib/Ryacas0_0.4.4.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
