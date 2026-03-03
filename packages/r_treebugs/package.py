# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreebugs(RPackage):
	"""Hierarchical Multinomial Processing Tree Modeling

	User-friendly analysis of hierarchical multinomial processing tree (MPT) 
    models that are often used in cognitive psychology. Implements the latent-trait 
    MPT approach (Klauer, 2010) <DOI:10.1007/s11336-009-9141-0> and the beta-MPT 
    approach (Smith & Batchelder, 2010) <DOI:10.1016/j.jmp.2009.06.007> to model 
    heterogeneity of participants. MPT models are conveniently specified by an
    .eqn-file as used by other MPT software and data are provided by a .csv-file 
    or directly in R. Models are either fitted by calling JAGS or by an MPT-tailored 
    Gibbs sampler in C++ (only for nonhierarchical and beta MPT models). Provides 
    tests of heterogeneity and MPT-tailored summaries and plotting functions.
    A detailed documentation is available in Heck, Arnold, & Arnold (2018) 
    <DOI:10.3758/s13428-017-0869-7> and a tutorial on MPT modeling can be found 
    in Schmidt, Erdfelder, & Heck (2022) <DOI:10.31234/osf.io/gh8md>.
	"""
	
	homepage = "https://github.com/danheck/TreeBUGS"
	cran = "TreeBUGS" 

	version("1.5.0", md5="5d202fa479301a4fba3d1f7d53f0b1e2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-logspline", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
