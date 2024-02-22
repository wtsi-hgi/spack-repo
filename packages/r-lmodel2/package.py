# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmodel2(RPackage):
	"""Model II Regression

	Computes model II simple linear regression using ordinary
 least squares (OLS), major axis (MA), standard major axis (SMA), and
 ranged major axis (RMA).
	"""
	
	cran = "lmodel2" 

	version("1.7-3", md5="95346e8507abb2380049cc4c2ec18b65", url="https://cran.r-project.org/src/contrib/lmodel2_1.7-3.tar.gz")

	depends_on("r@2.14:", type=("build", "run"))
