# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodacore(RPackage):
	"""Learning Sparse Log-Ratios for Compositional Data

	In the context of high-throughput genetic data,
    CoDaCoRe identifies a set of sparse biomarkers that are
    predictive of a response variable of interest (Gordon-Rodriguez 
    et al., 2021) <doi:10.1093/bioinformatics/btab645>. More 
    generally, CoDaCoRe can be applied to any regression problem 
    where the independent variable is Compositional (CoDa), to 
    derive a set of scale-invariant log-ratios (ILR or SLR) that 
    are maximally associated to a dependent variable.
	"""
	
	cran = "codacore" 

	version("0.0.4", md5="3705c4ff2ccab4c9caa8a814d6487039")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tensorflow@2.1:", type=("build", "run"))
	depends_on("r-keras@2.3:", type=("build", "run"))
	depends_on("r-proc@1.17:", type=("build", "run"))
	depends_on("r-r6@2.5:", type=("build", "run"))
	depends_on("r-gtools@3.8:", type=("build", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
