# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogconcens(RPackage):
	"""Maximum Likelihood Estimation of a Log-Concave Density Based on
Censored Data

	Based on right or interval censored data, compute the maximum likelihood estimator of a (sub)probability density under the assumption that it is log-concave. For further information see Duembgen, Rufibach and Schuhmacher (2014) <doi:10.1214/14-EJS930>.
	"""
	
	cran = "logconcens" 

	version("0.17-3", md5="f72849e47ae9bb811e052c43932ae74d")

	depends_on("r@2.15:", type=("build", "run"))
