# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevdbayes(RPackage):
	"""Ratio-of-Uniforms Sampling for Bayesian Extreme Value Analysis

	Provides functions for the Bayesian analysis of extreme value
    models.  The 'rust' package <https://cran.r-project.org/package=rust> is
    used to simulate a random sample from the required posterior distribution.
    The functionality of 'revdbayes' is similar to the 'evdbayes' package
    <https://cran.r-project.org/package=evdbayes>, which uses Markov Chain
    Monte Carlo ('MCMC') methods for posterior simulation.  In addition, there
    are functions for making inferences about the extremal index, using 
    the models for threshold inter-exceedance times of Suveges and Davison 
    (2010) <doi:10.1214/09-AOAS292> and Holesovsky and Fusek (2020) 
    <doi:10.1007/s10687-020-00374-3>. Also provided are d,p,q,r functions for 
    the Generalised Extreme Value ('GEV') and Generalised Pareto ('GP') 
    distributions that deal appropriately with cases where the shape parameter 
    is very close to zero.
	"""
	
	homepage = "https://paulnorthrop.github.io/revdbayes/"
	cran = "revdbayes" 

	version("1.5.3", md5="f19c7af715a6a845ca9a615276bc4603")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bayesplot@1.1:", type=("build", "run"))
	depends_on("r-exdex", type=("build", "run"))
	depends_on("r-rcpp@0.12.10:", type=("build", "run"))
	depends_on("r-rust@1.2.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
