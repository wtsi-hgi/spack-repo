# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhase123(RPackage):
	"""Simulating and Conducting Phase 123 Trials

	Contains three simulation functions for implementing the entire Phase 123 trial and the separate Eff-Tox and Phase 3 portions of the trial, which may be beneficial for use on clusters. The functions AssignEffTox() and RandomizeEffTox() assign doses to patient cohorts during phase 12 and Reoptimize() determines the optimal dose to continue with during Phase 3. The functions ReturnMeansAgent() and ReturnMeanControl() gives the true mean survival for the agent doses and control and ReturnOCS() gives the operating characteristics of the design.
	"""
	
	cran = "Phase123" 

	version("2.1", md5="a686e48a92cb0b647068bc355040693c", url="https://cran.r-project.org/src/contrib/Phase123_2.1.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
