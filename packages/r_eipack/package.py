# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REipack(RPackage):
	"""Ecological Inference and Higher-Dimension Data Management

	Provides methods for analyzing R by C ecological contingency
        tables using the extreme case analysis, ecological regression,
        and Multinomial-Dirichlet ecological inference models.  Also
        provides tools for manipulating higher-dimension data objects.
	"""
	
	homepage = "http://www.olivialau.org/software/"
	cran = "eiPack" 

	version("0.2-2", md5="78b63a0c417ef20ebbedfd7c5635454b")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
