# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandtoolbox(RPackage):
	"""Toolbox for Pseudo and Quasi Random Number Generation and Random
Generator Tests

	Provides (1) pseudo random generators - general linear congruential generators, 
    multiple recursive generators and generalized feedback shift register (SF-Mersenne Twister
    algorithm (<doi:10.1007/978-3-540-74496-2_36>) and WELL (<doi:10.1145/1132973.1132974>) 
    generators); (2) quasi random generators - the Torus algorithm, the
    Sobol sequence, the Halton sequence (including the Van der Corput sequence) and (3) some
    generator tests - the gap test, the serial test, the poker test, see, e.g., 
    Gentle (2003) <doi:10.1007/b97336>. 
    Take a look at the Distribution task view of types and tests of random number generators.
    The package can be provided without the 'rngWELL' dependency on demand.
    Package in Memoriam of Diethelm and Barbara Wuertz.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/rmetrics/"
	cran = "randtoolbox" 

	version("2.0.4", md5="a17ceb0e2e5062191249235e50e832f6")

	depends_on("r-rngwell@0.10.1:", type=("build", "run"))
