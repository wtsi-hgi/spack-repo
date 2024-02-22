# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpc(RPackage):
	"""Statistical Process Control -- Calculation of ARL and Other
Control Chart Performance Measures

	Evaluation of control charts by means of
        the zero-state, steady-state ARL (Average Run Length) and RL quantiles.
        Setting up control charts for given in-control ARL. The control charts
        under consideration are one- and two-sided EWMA, CUSUM, and
        Shiryaev-Roberts schemes for monitoring the mean or variance of normally
        distributed independent data. ARL calculation of the same set of schemes under drift (in the mean) are added.
        Eventually, all ARL measures for the multivariate EWMA (MEWMA) are provided.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "spc" 

	version("0.6.7", md5="758bf6ca1717d461b05ee97fa47d51a0")

	depends_on("r@1.8:", type=("build", "run"))
