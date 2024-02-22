# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoala(RPackage):
	"""A Framework for Coalescent Simulation

	Coalescent simulators can rapidly simulate biological sequences
    evolving according to a given model of evolution.
    You can use this package to specify such models, to conduct the simulations
    and to calculate additional statistics from the results (Staab, Metzler,
    2016 <doi:10.1093/bioinformatics/btw098>).
    It relies on existing simulators for doing the simulation, and currently
    supports the programs 'ms', 'msms' and 'scrm'. It also supports finite-sites
    mutation models by combining the simulators with the program 'seq-gen'.
    Coala provides functions for calculating certain summary statistics, which
    can also be applied to actual biological data.
    One possibility to import data is through the 'PopGenome' package
    (<https://github.com/pievos101/PopGenome>).
	"""
	
	homepage = "https://github.com/statgenlmu/coala"
	cran = "coala" 

	version("0.7.1", md5="30a2f497cc54646965e30c7d6f67a375")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-r6@2.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rehh@3:", type=("build", "run"))
	depends_on("r-scrm@1.6.0.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.3.810:", type=("build", "run"))
