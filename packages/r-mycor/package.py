# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMycor(RPackage):
	"""Automatic Correlation and Regression Test in a 'data.frame'

	Perform correlation and linear regression test
    among the numeric fields in a data.frame automatically
    and make plots using pairs or lattice::parallelplot.
	"""
	
	homepage = "https://github.com/cardiomoon/mycor"
	cran = "mycor" 

	version("0.1.1", md5="aecd9c7af470b5c148a9e2e3d4a34b45")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
