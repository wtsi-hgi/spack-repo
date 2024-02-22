# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRajive(RPackage):
	"""Robust Angle Based Joint and Individual Variation Explained

	A robust alternative to the aJIVE (angle based Joint and Individual Variation Explained) method (Feng et al 2018: <doi:10.1016/j.jmva.2018.03.008>) for the estimation of joint and individual components in the presence of outliers in multi-source data. It decomposes the multi-source data into joint, individual and residual (noise) contributions. The decomposition is robust to outliers and noise in the data. The method is illustrated in Ponzi et al (2021) <arXiv:2101.09110>.
	"""
	
	cran = "RaJIVE" 

	version("1.0", md5="656c9306ced8effcf2f54593f8245f52")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
