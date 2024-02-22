# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNls2(RPackage):
	"""Non-Linear Regression with Brute Force

	Adds brute force and multiple starting values to nls.
	"""
	
	homepage = "https://github.com/ggrothendieck/nls2"
	cran = "nls2" 

	version("0.3-3", md5="eee678502a3619729c92e99af2aec30d", url="https://cran.r-project.org/src/contrib/nls2_0.3-3.tar.gz")

	depends_on("r-proto", type=("build", "run"))
