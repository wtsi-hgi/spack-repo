# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriplesmatch(RPackage):
	"""Match Triples Consisting of Two Controls and a Treated Unit or
Vice Versa

	Attain excellent covariate balance by matching two treated units
    and one control unit or vice versa within strata. Using such triples, as
    opposed to also allowing pairs of treated and control units, 
    allows easier interpretation of the two possible 
    weights of observations and better insensitivity to unmeasured bias in the test
    statistic. Using triples instead of matching in a fixed 1:2 or 2:1 ratio
    allows for the match to be feasible in more situations.
    The 'rrelaxiv' package, which provides an alternative solver for the underlying 
    network flow problems, carries an academic license and is not available on CRAN, but
    may be downloaded from 'GitHub' at <https://github.com/josherrickson/rrelaxiv/>.
    The 'Gurobi' commercial optimization software is required to use the two functions
    [infsentrip()] and [triplesIP()]. These functions are not essential
    to the main purpose of this package. A free academic license can be obtained at 
    <https://www.gurobi.com/features/academic-named-user-license/>. 
    The 'gurobi' R package can then be installed following 
    the instructions at <https://www.gurobi.com/documentation/9.1/refman/ins_the_r_package.html>.
	"""
	
	cran = "triplesmatch" 

	version("1.0.0", md5="8f4424f56c66c5b4be84f923849d9943")

	depends_on("r-rcbalance", type=("build", "run"))
	depends_on("r-rlemon", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-optmatch", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
