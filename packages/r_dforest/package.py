# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDforest(RPackage):
	"""Decision Forest

	Provides R-implementation of Decision forest algorithm, which combines the predictions of
    multiple independent decision tree models for a consensus decision. In particular, Decision Forest is a novel 
    pattern-recognition method which can be used to analyze: (1) DNA microarray data; 
    (2) Surface-Enhanced Laser Desorption/Ionization Time-of-Flight Mass Spectrometry  (SELDI-TOF-MS) data; and 
    (3) Structure-Activity Relation (SAR) data.
    In this package, three fundamental functions are provided, as (1)DF_train, (2)DF_pred, and (3)DF_CV.  
    run Dforest() to see more instructions.
    Weida Tong (2003) <doi:10.1021/ci020058s>.
	"""
	
	cran = "Dforest" 

	version("0.4.2", md5="82144d37cb5f7910b481ce84eaf8a3a2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
