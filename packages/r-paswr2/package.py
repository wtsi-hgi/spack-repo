# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaswr2(RPackage):
	"""Probability and Statistics with R, Second Edition

	Functions and data sets for the text Probability and Statistics
    with R, Second Edition.
	"""
	
	homepage = "https://github.com/alanarnholt/PASWR2"
	cran = "PASWR2" 

	version("1.0.5", md5="6225449f230b07fc0671039e60bc61c2", url="https://cran.r-project.org/src/contrib/PASWR2_1.0.5.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
