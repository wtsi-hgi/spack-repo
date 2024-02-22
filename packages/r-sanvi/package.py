# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanvi(RPackage):
	"""Fitting Shared Atoms Nested Models via Variational Bayes

	An efficient tool for fitting the nested common and shared atoms models using variational Bayes approximate inference for fast computation. Specifically, the package implements the common atoms model (Denti et al., 2023), its finite version (D'Angelo et al., 2023), and a hybrid finite-infinite model. 
            All models use Gaussian mixtures with a normal-inverse-gamma prior distribution on the parameters. Additional functions are provided to help analyze the results of the fitting procedure.  
            References:   
            Denti, Camerlenghi, Guindani, Mira (2023) <doi:10.1080/01621459.2021.1933499>,    
            D’Angelo, Canale, Yu, Guindani (2023) <doi:10.1111/biom.13626>.
	"""
	
	homepage = "https://github.com/fradenti/SANvi"
	cran = "SANvi" 

	version("0.1.0", md5="271fd8e2d4755eb4e55c26e996b2f465")

	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
