# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStopp(RPackage):
	"""Spatio-Temporal Point Pattern Methods, Model Fitting,
Diagnostics, Simulation, Local Tests

	Toolbox for different kinds of spatio-temporal analyses to be performed on observed point patterns, following the growing stream of literature on point process theory. This R package implements functions to perform different kinds of analyses on point processes, proposed in the papers (Siino, Adelfio, and Mateu 2018<doi:10.1007/s00477-018-1579-0>; Siino et al. 2018<doi:10.1002/env.2463>; Adelfio et al. 2020<doi:10.1007/s00477-019-01748-1>; D’Angelo, Adelfio, and Mateu 2021<doi:10.1016/j.spasta.2021.100534>; D’Angelo, Adelfio, and Mateu 2022<doi:10.1007/s00362-022-01338-4>; D’Angelo, Adelfio, and Mateu 2023<doi:10.1016/j.csda.2022.107679>). The main topics include modeling, statistical inference, and simulation issues on spatio-temporal point processes on Euclidean space and linear networks.
	"""
	
	cran = "stopp" 

	version("0.1.1", md5="afd5b6d08fe823cc6129fc0b7c2f85ef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-sparr", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-linnet", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-stlnpp", type=("build", "run"))
	depends_on("r-stpp", type=("build", "run"))
	depends_on("r-etasflp", type=("build", "run"))
