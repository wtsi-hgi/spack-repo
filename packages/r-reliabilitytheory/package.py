# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReliabilitytheory(RPackage):
	"""Structural Reliability Analysis

	Perform structural reliability analysis, including computation and
    simulation with system signatures, Samaniego (2007)
    <doi:10.1007/978-0-387-71797-5>, and survival signatures, Coolen and
    Coolen-Maturi (2013) <doi:10.1007/978-3-642-30662-4_8>. Additionally
    supports parametric and topological inference given system lifetime data,
    Aslett (2012) <https://www.louisaslett.com/PhD_Thesis.pdf>.
	"""
	
	homepage = "https://www.louisaslett.com/"
	cran = "ReliabilityTheory" 

	version("0.3.0", md5="da717d98de782ca3f7a4dfd01a4f01dc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-fraction", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-mcmc", type=("build", "run"))
	depends_on("r-phasetype@0.2:", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
