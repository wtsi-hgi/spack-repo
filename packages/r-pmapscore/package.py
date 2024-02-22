# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmapscore(RPackage):
	"""Identify Prognosis-Related Pathways Altered by Somatic Mutation

	We innovatively defined a pathway mutation accumulate perturbation score (PMAPscore) to reflect the position and the cumulative effect of the genetic mutations at the pathway level. Based on the PMAPscore of pathways, identified prognosis-related pathways altered by somatic mutation and predict immunotherapy efficacy by constructing a multiple-pathway-based risk model (Tarca, Adi Laurentiu et al (2008) <doi:10.1093/bioinformatics/btn577>).
	"""
	
	cran = "PMAPscore" 

	version("0.1.1", md5="46d26b7b4b17c24a1410a67e4dbef7f9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
