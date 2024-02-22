# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReservoir(RPackage):
	"""Tools for Analysis, Design, and Operation of Water Supply
Storages

	Measure single-storage water supply system performance using resilience,
    reliability, and vulnerability metrics; assess storage-yield-reliability
    relationships; determine no-fail storage with sequent peak analysis; optimize
    release decisions for water supply, hydropower, and multi-objective reservoirs
    using deterministic and stochastic dynamic programming; generate inflow
    replicates using parametric and non-parametric models; evaluate inflow
    persistence using the Hurst coefficient.
	"""
	
	homepage = "https://cran.r-project.org/package=reservoir"
	cran = "reservoir" 

	version("1.1.5", md5="f0d4fb49233db9ae4d84c276c1886178")

	depends_on("r-gtools", type=("build", "run"))
