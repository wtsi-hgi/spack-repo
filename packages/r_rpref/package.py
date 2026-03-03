# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpref(RPackage):
	"""Database Preferences and Skyline Computation

	Routines to select and visualize the maxima for a given strict
    partial order. This especially includes the computation of the Pareto
    frontier, also known as (Top-k) Skyline operator (see Börzsönyi, et al. 
    (2001) <doi:10.1109/ICDE.2001.914855>), and some generalizations 
    known as database preferences (see Kießling (2002) 
    <doi:10.1016/B978-155860869-6/50035-4>).
	"""
	
	homepage = "https://www.p-roocks.de/rpref/"
	cran = "rPref" 

	version("1.4.0", md5="0ccb5ebbd5143f4a25fb38900bf84f64")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-lazyeval@0.2.1:", type=("build", "run"))
