# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdpsurvival(RPackage):
	"""Imprecise Dirichlet Process for Survival Analysis

	Functions to perform robust
		 nonparametric survival analysis with right censored 
		 data using a prior near-ignorant Dirichlet Process.
		 Mangili, F., Benavoli, A., de Campos, C.P., Zaffalon, M. (2015) <doi:10.1002/bimj.201500062>.
	"""
	
	homepage = "http://ipg.idsia.ch/software/"
	cran = "IDPSurvival" 

	version("1.2", md5="3c48aed65d460d248ebb63b181d788d5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
