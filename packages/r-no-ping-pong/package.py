# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoPingPong(RPackage):
	"""Incorporating Previous Findings When Evaluating New Data

	Functions for revealing what happens when effect size estimates 
    from previous studies are taken into account when evaluating each new dataset 
    in a study sequence. The analyses can be conducted for cumulative
    meta-analyses and for Bayesian data analyses. The package contains sample 
    data for a wide selection of research topics. Jointly considering 
    previous findings along with new data is more likely to result in correct 
    conclusions than does the traditional practice of not incorporating previous
    findings, which often results in a back and forth ping-pong of conclusions 
    when evaluating a sequence of studies.
    O'Connor & Ermacora (2021, <doi:10.3758/bf03200807>).
	"""
	
	cran = "NO.PING.PONG" 

	version("0.1.6", md5="5d85e82bbd89f0c779fc1638563cf62c")

	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-mcmcglmm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
