# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpboottprmfbar(RPackage):
	"""Informative Nonparametric Bootstrap Test with Pooled Resampling

	Sample sizes are often small due to hard to reach target populations,
    rare target events, time constraints, limited budgets, or ethical considerations.
    Two statistical methods with promising performance in small samples are the
    nonparametric bootstrap test with pooled resampling method, which is the
    focus of Dwivedi, Mallawaarachchi, and Alvarado (2017) <doi:10.1002/sim.7263>,
    and informative hypothesis testing, which is implemented in the 'restriktor'
    package. The 'npboottprmFBar' package uses the nonparametric bootstrap test
    with pooled resampling method to implement informative hypothesis testing.
    The bootFbar() function can be used to analyze data with this method and the
    persimon() function can be used to conduct performance simulations on type-one
    error and statistical power.
	"""
	
	homepage = "https://github.com/mightymetrika/npboottprmFBar"
	cran = "npboottprmFBar" 

	version("0.1.1", md5="90d1a20e77b5f4bc8b42cd4e106cfff7")

	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-lmperm", type=("build", "run"))
	depends_on("r-npboottprm", type=("build", "run"))
	depends_on("r-restriktor", type=("build", "run"))
