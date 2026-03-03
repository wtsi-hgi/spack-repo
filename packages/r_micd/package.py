# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicd(RPackage):
	"""Multiple Imputation in Causal Graph Discovery

	Modified functions of the package 'pcalg' and some additional functions
            to run the PC and the FCI (Fast Causal Inference) algorithm for constraint-based 
            causal discovery in incomplete and multiply imputed datasets.
            Foraita R, Friemel J, Günther K, Behrens T, Bullerdiek J, Nimzyk R, Ahrens W, Didelez V (2020) <doi:10.1111/rssa.12565>;
            Andrews RM, Foraita R, Didelez V, Witte J (2021) <arXiv:2108.13395>; Witte J, Foraita R, Didelez V (2022) <doi:10.1002/sim.9535>.
	"""
	
	homepage = "https://github.com/bips-hb/micd"
	cran = "micd" 

	version("1.1.1", md5="f6e1eb8a3c7842273a36f627baa11600")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
