# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgdrive2(RPackage):
	"""Mosquito Gene Drive Explorer 2

	A simulation modeling framework which significantly extends capabilities from the
    'MGDrivE' simulation package via a new mathematical and computational framework based on stochastic Petri nets.
    For more information about 'MGDrivE', see our publication: Sánchez et al. (2019) <doi:10.1111/2041-210X.13318>
    Some of the notable capabilities of 'MGDrivE2' include: incorporation of human populations,
    epidemiological dynamics, time-varying parameters, and a continuous-time simulation
    framework with various sampling algorithms for both deterministic and stochastic interpretations.
    'MGDrivE2' relies on the genetic inheritance structures provided in package 'MGDrivE', so we
    suggest installing that package initially.
	"""
	
	homepage = "https://marshalllab.github.io/MGDrivE/docs_v2/index.html"
	cran = "MGDrivE2" 

	version("2.1.0", md5="d2a9ad7bd0fd6a502364f36c8110bad5", url="https://cran.r-project.org/src/contrib/MGDrivE2_2.1.0.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
