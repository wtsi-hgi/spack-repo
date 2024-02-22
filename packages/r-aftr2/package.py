# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAftr2(RPackage):
	"""R-Squared Measure under Accelerated Failure Time (AFT) Models

	Compute the R-squared measure under the accelerated failure time (AFT) models proposed in Chan et. al. (2018) <doi:10.1080/03610918.2016.1177072>.
	"""
	
	cran = "aftR2" 

	version("0.1.0", md5="e3c69463ad5c8f7e73573d72e7fa840e", url="https://cran.r-project.org/src/contrib/aftR2_0.1.0.tar.gz")

	depends_on("r-survival", type=("build", "run"))
