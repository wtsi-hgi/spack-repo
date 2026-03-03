# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSirt(RPackage):
	"""Supplementary Item Response Theory Models

	
    Supplementary functions for item response models aiming
    to complement existing R packages. The functionality includes among others
    multidimensional compensatory and noncompensatory IRT models
    (Reckase, 2009, <doi:10.1007/978-0-387-89976-3>), 
    MCMC for hierarchical IRT models and testlet models
    (Fox, 2010, <doi:10.1007/978-1-4419-0742-4>), 
    NOHARM (McDonald, 1982, <doi:10.1177/014662168200600402>), 
    Rasch copula model (Braeken, 2011, <doi:10.1007/s11336-010-9190-4>;
    Schroeders, Robitzsch & Schipolowski, 2014, <doi:10.1111/jedm.12054>),
    faceted and hierarchical rater models (DeCarlo, Kim & Johnson, 2011,
    <doi:10.1111/j.1745-3984.2011.00143.x>),
    ordinal IRT model (ISOP; Scheiblechner, 1995, <doi:10.1007/BF02301417>), 
    DETECT statistic (Stout, Habing, Douglas & Kim, 1996, 
    <doi:10.1177/014662169602000403>), local structural equation modeling 
    (LSEM; Hildebrandt, Luedtke, Robitzsch, Sommer & Wilhelm, 2016,
    <doi:10.1080/00273171.2016.1142856>).
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/sirt"
	cran = "sirt" 

	version("4.1-15", md5="69dbcccebadea5ab4f84bd426b1970ab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cdm", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tam", type=("build", "run"))
	depends_on("r-pbv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
