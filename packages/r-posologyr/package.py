# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPosologyr(RPackage):
	"""Individual Dose Optimization using Population Pharmacokinetics

	Determine individual pharmacokinetic (and
    pharmacokinetic-pharmacodynamic) profiles and use them to personalise drug
    regimens. You provide the data and a population pharmacokinetic model,
    'posologyr' provides the individual a posteriori estimate and allows you to
    determine the optimal dosing. The empirical Bayes estimates are computed as
    described in Kang et al. (2012) <doi:10.4196/kjpp.2012.16.2.97>.
	"""
	
	homepage = "https://levenc.github.io/posologyr/"
	cran = "posologyr" 

	version("1.2.4", md5="773fbabd527bca77507a59e31fa51c33")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rxode2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
