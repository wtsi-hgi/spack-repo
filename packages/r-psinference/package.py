# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsinference(RPackage):
	"""Inference for Released Plug-in Sampling Single Synthetic Dataset

	Considering the singly imputed synthetic data generated via plug-in sampling under the multivariate normal model, draws inference procedures including the generalized variance, the sphericity test, the test for independence between two subsets of variables, and the test for the regression of one set of variables on the other. For more details see Klein et al. (2021) <doi:10.1007/s13571-019-00215-9>.
	"""
	
	homepage = "https://github.com/ricardomourarpm/PSinference"
	cran = "PSinference" 

	version("0.1.0", md5="47127087d01e0e741c42d4d20cc718cc")

	depends_on("r-mass", type=("build", "run"))
