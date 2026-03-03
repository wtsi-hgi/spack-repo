# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsica(RPackage):
	"""Decision Tree Analysis for Probabilistic Subgroup Identification
with Multiple Treatments

	In the situation when multiple alternative treatments or
    interventions available, different population groups may respond differently
    to different treatments. This package implements a method that discovers
    the population subgroups in which a certain treatment has a better effect
    than the other alternative treatments. This is done by first estimating the
    treatment effect for a given treatment and its uncertainty by computing random
    forests, and the resulting model is summarized by a decision tree in which the
    probabilities that the given treatment is best for a given subgroup is shown in
    the corresponding terminal node of the tree.
	"""
	
	cran = "psica" 

	version("1.0.2", md5="f96397245c7ccc600d14674986ec9cab")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-bayestree", type=("build", "run"))
