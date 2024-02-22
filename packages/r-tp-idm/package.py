# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpIdm(RPackage):
	"""Estimation of Transition Probabilities for the Illness-Death
Model

	Estimation of transition probabilities for the illness-death model. Both the Aalen-Johansen estimator for a Markov model and a novel non-Markovian estimator by de Una-Alvarez and Meira-Machado (2015) <doi:10.1111/biom.12288>, see also Balboa and de Una-Alvarez (2018) <doi:10.18637/jss.v083.i10>, are included.
	"""
	
	cran = "TP.idm" 

	version("1.5.1", md5="1edb1e78ef87d8e67499e8c7c526b05e")

	depends_on("r@3.1.1:", type=("build", "run"))
