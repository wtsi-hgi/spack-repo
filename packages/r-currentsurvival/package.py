# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurrentsurvival(RPackage):
	"""Estimation of CCI and CLFS Functions

	The currentSurvival package contains functions for
  the estimation of the current cumulative incidence (CCI) and
  the current leukaemia-free survival (CLFS). The CCI is the 
  probability that a patient is alive and in any disease 
  remission (e.g. complete cytogenetic remission in chronic 
  myeloid leukaemia) after initiating his or her therapy (e.g. 
  tyrosine kinase therapy for chronic myeloid leukaemia). The 
  CLFS is the probability that a patient is alive and in any 
  disease remission after achieving the first disease remission.
	"""
	
	cran = "currentSurvival" 

	version("1.1", md5="d427c35573a6c0edbe0c36c30593a8c9")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
