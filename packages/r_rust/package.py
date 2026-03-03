# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRust(RPackage):
	"""Ratio-of-Uniforms Simulation with Transformation

	Uses the generalized ratio-of-uniforms (RU) method to simulate
    from univariate and (low-dimensional) multivariate continuous distributions.
    The user specifies the log-density, up to an additive constant. The RU
    algorithm is applied after relocation of mode of the density to zero, and
    the user can choose a tuning parameter r. For details see Wakefield, Gelfand
    and Smith (1991) <DOI:10.1007/BF01889987>, Efficient generation of random
    variates via the ratio-of-uniforms method, Statistics and Computing (1991)
    1, 129-133.  A Box-Cox variable transformation can be used to make the input
    density suitable for the RU method and to improve efficiency.  In the
    multivariate case rotation of axes can also be used to improve efficiency.
    From version 1.2.0 the 'Rcpp' package 
    <https://cran.r-project.org/package=Rcpp> can be used to improve efficiency.
	"""
	
	homepage = "https://paulnorthrop.github.io/rust/"
	cran = "rust" 

	version("1.4.2", md5="50a94d316fe586446812ab92a4a3e9cc")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12.10:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
