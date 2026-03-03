# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenalizedsvm(RPackage):
	"""Feature Selection SVM using Penalty Functions

	Support Vector Machine (SVM) classification with simultaneous feature selection using penalty
        functions is implemented. The smoothly clipped absolute deviation (SCAD),
        'L1-norm', 'Elastic Net' ('L1-norm' and 'L2-norm') and 'Elastic
        SCAD' (SCAD and 'L2-norm') penalties are available. The tuning
        parameters can be found using either a fixed grid or a interval
        search.
	"""
	
	cran = "penalizedSVM" 

	version("1.1.4", md5="0cd780813457f2f19412af2dc87b7789")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mlegp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-tgp", type=("build", "run"))
