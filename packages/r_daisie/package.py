# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaisie(RPackage):
	"""Dynamical Assembly of Islands by Speciation, Immigration and
Extinction

	Simulates and computes the (maximum) likelihood of a dynamical 
    model of island biota assembly through speciation, immigration and
    extinction. See Valente et al. (2015) <doi:10.1111/ele.12461>.
	"""
	
	homepage = "https://github.com/rsetienne/DAISIE"
	cran = "DAISIE" 

	version("4.4.1", md5="7da56e03b9ec59c3a27cb20b2b887f96")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-ddd@5:", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh@1.81.0.1:", type=("build", "run"))
