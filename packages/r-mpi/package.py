# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpi(RPackage):
	"""Computation of Multidimensional Poverty Index (MPI)

	Computing package for Multidimensional Poverty Index (MPI) using Alkire-Foster method. Given N individuals, each person has D indicators of deprivation, the package compute MPI value to represent the degree of poverty in a population. The inputs are 1) an N by D matrix, which has the element (i,j) represents whether an individual i is deprived in an indicator j (1 is deprived and 0 is not deprived), and 2) the deprivation threshold.  The main output is the MPI value, which has the range between zero and one. MPI value is approaching one if almost all people are deprived in all indicators, and it is approaching zero if almost no people are deprived in any indicator.  Please see Alkire S., Chatterjee, M., Conconi, A., Seth, S. and Ana Vaz (2014) <doi:10.35648/20.500.12413/11781/ii039> for The Alkire-Foster methodology.
	"""
	
	homepage = "https://github.com/9POINTEIGHT/MPI"
	cran = "MPI" 

	version("0.1.0", md5="0f9ce5c0c4047c64aac0d64d701ea547")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
