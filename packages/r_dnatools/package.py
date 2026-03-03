# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnatools(RPackage):
	"""Tools for Analysing Forensic Genetic DNA Data

	Computationally efficient tools for comparing all pairs of profiles
    in a DNA database. The expectation and covariance of the summary statistic
    is implemented for fast computing. Routines for estimating proportions of
    close related individuals are available. The use of wildcards (also called F-
    designation) is implemented. Dedicated functions ease plotting the results. 
    See Tvedebrink et al. (2012) <doi:10.1016/j.fsigen.2011.08.001>. 
    Compute the distribution of the numbers of alleles in DNA mixtures. 
    See Tvedebrink (2013) <doi:10.1016/j.fsigss.2013.10.142>.
	"""
	
	cran = "DNAtools" 

	version("0.2-4", md5="d2b2c803ed1bef3c46f00d3ebd367ac6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rsolnp@1.16:", type=("build", "run"))
	depends_on("r-multicool@0.1.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
