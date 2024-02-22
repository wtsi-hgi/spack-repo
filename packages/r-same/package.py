# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSame(RPackage):
	"""Seamless Adaptive Multi-Arm Multi-Stage Enrichment

	Design a Bayesian seamless multi-arm biomarker-enriched phase II/III 
             design with the survival endpoint with allowing sample size re-estimation.
             James M S Wason, Jean E Abraham, Richard D Baird, Ioannis Gournaris, Anne-Laure Vallier, James D Brenton, Helena M Earl, Adrian P Mander (2015) <doi:10.1038/bjc.2015.278>.
             Guosheng Yin, Nan Chen, J. Jack Lee (2018) <doi:10.1007/s12561-017-9199-7>.
             Ying Yuan, Beibei Guo, Mark Munsell, Karen Lu, Amir Jazaeri (2016) <doi:10.1002/sim.6971>.
	"""
	
	cran = "SAME" 

	version("0.1.0", md5="c1843bf1c2ee1e9cfbfdda238bfaee7a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
