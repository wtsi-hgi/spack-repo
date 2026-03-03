# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPotential(RPackage):
	"""Implementation of the Potential Model

	Provides functions to compute the potential model as defined by
    Stewart (1941) <doi:10.1126/science.93.2404.89>. Several options are available
    to customize the model, such as the possibility to fine-tune the distance
    friction functions or to use custom distance matrices. Some computations are
    parallelized to improve their efficiency.
	"""
	
	homepage = "https://github.com/riatelab/potential"
	cran = "potential" 

	version("0.2.0", md5="6f2cb7287323a13811aa038f4cd64f02")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-mapiso", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
