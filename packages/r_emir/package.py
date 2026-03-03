# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmir(RPackage):
	"""Evolutionary Minimizer for R

	A C++ implementation of the following evolutionary
    algorithms: Bat Algorithm (Yang, 2010 <doi:10.1007/978-3-642-12538-6_6>),
    Cuckoo Search (Yang, 2009 <doi:10.1109/nabic.2009.5393690>),
    Genetic Algorithms (Holland, 1992, ISBN:978-0262581110),
    Gravitational Search Algorithm (Rashedi et al., 2009 <doi:10.1016/j.ins.2009.03.004>),
    Grey Wolf Optimization (Mirjalili et al., 2014 <doi:10.1016/j.advengsoft.2013.12.007>),
    Harmony Search (Geem et al., 2001 <doi:10.1177/003754970107600201>),
    Improved Harmony Search (Mahdavi et al., 2007 <doi:10.1016/j.amc.2006.11.033>),
    Moth-flame Optimization (Mirjalili, 2015 <doi:10.1016/j.knosys.2015.07.006>),
    Particle Swarm Optimization (Kennedy et al., 2001 ISBN:1558605959),
    Simulated Annealing (Kirkpatrick et al., 1983 <doi:10.1126/science.220.4598.671>),
    Whale Optimization Algorithm (Mirjalili and Lewis, 2016 <doi:10.1016/j.advengsoft.2016.01.008>).
    'EmiR' can be used not only for unconstrained optimization problems, but also
    in presence of inequality constrains, and variables restricted to be integers.
	"""
	
	cran = "EmiR" 

	version("1.0.4", md5="ff5e4462e152410150304ba48aae41d9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
