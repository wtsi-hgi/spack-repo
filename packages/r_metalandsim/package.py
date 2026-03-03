# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetalandsim(RPackage):
	"""Landscape and Range Expansion Simulation

	Tools to generate random landscape graphs, evaluate species
    occurrence in dynamic landscapes, simulate future landscape occupation and
    evaluate range expansion when new empty patches are available (e.g. as a
    result of climate change). References: Mestre, F., Canovas, F., Pita, R., 
    Mira, A., Beja, P. (2016) <doi:10.1016/j.envsoft.2016.03.007>; Mestre, F., 
    Risk, B., Mira, A., Beja, P., Pita, R. (2017) 
    <doi:10.1016/j.ecolmodel.2017.06.013>; Mestre, F., Pita, R., Mira, A., Beja,
    P. (2020) <doi:10.1186/s12898-019-0273-5>.
	"""
	
	cran = "MetaLandSim" 

	version("2.0.0", md5="e86409d2289d1e9d7f2da3c3a9cc1cb2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-zipfr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
