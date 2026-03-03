# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaheuristicopt(RPackage):
	"""Metaheuristic for Optimization

	An implementation of metaheuristic algorithms for continuous optimization. Currently, the package contains the implementations of 21 algorithms, as follows: particle swarm optimization (Kennedy and Eberhart, 1995), ant lion optimizer (Mirjalili, 2015 <doi:10.1016/j.advengsoft.2015.01.010>), grey wolf optimizer (Mirjalili et al., 2014 <doi:10.1016/j.advengsoft.2013.12.007>), dragonfly algorithm (Mirjalili, 2015 <doi:10.1007/s00521-015-1920-1>), firefly algorithm (Yang, 2009 <doi:10.1007/978-3-642-04944-6_14>), genetic algorithm (Holland, 1992, ISBN:978-0262581110), grasshopper optimisation algorithm (Saremi et al., 2017 <doi:10.1016/j.advengsoft.2017.01.004>), harmony search algorithm (Mahdavi et al., 2007 <doi:10.1016/j.amc.2006.11.033>), moth flame optimizer (Mirjalili, 2015 <doi:10.1016/j.knosys.2015.07.006>, sine cosine algorithm (Mirjalili, 2016 <doi:10.1016/j.knosys.2015.12.022>),  whale optimization algorithm (Mirjalili and Lewis, 2016 <doi:10.1016/j.advengsoft.2016.01.008>), clonal selection algorithm (Castro, 2002 <doi:10.1109/TEVC.2002.1011539>), differential evolution (Das & Suganthan, 2011), shuffled frog leaping (Eusuff, Landsey & Pasha, 2006), cat swarm optimization (Chu et al., 2006), artificial bee colony algorithm (Karaboga & Akay, 2009), krill-herd algorithm (Gandomi & Alavi, 2012), cuckoo search (Yang & Deb, 2009), bat algorithm (Yang, 2012), gravitational based search (Rashedi et al., 2009) and black hole optimization (Hatamlou, 2013).
	"""
	
	cran = "metaheuristicOpt" 

	version("2.0.0", md5="3e9456c5b90432db64e89e1e57b9fe71")

	depends_on("r@3.5:", type=("build", "run"))
