# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrindt(RPackage):
	"""Prediction and Interpretation in Decision Trees for
Classification and Regression

	Optimization of conditional inference trees from the package 'party'
    for classification and regression.
    For optimization, the model space is searched for the best tree on the full sample by 
    means of repeated subsampling. Restrictions are allowed so that only trees are accepted 
    which do not include pre-specified uninterpretable split results (cf. Weihs & Buschfeld, 2021a).
    The function PrInDT() represents the basic resampling loop for 2-class classification (cf. Weihs 
    & Buschfeld, 2021a). The function RePrInDT() (repeated PrInDT()) allows for repeated  
    applications of PrInDT() for different percentages of the observations of the large and the 
    small classes (cf. Weihs & Buschfeld, 2021c). The function NesPrInDT() (nested PrInDT()) 
    allows for an extra layer of subsampling for a specific factor variable (cf. Weihs & Buschfeld, 
    2021b). The functions PrInDTMulev() and PrInDTMulab() deal with multilevel and multilabel 
    classification. In addition to these PrInDT() variants for classification, the function 
    PrInDTreg() has been developed for regression problems. Finally, the function PostPrInDT() 
    allows for a posterior analysis of the distribution of a specified variable in the terminal 
    nodes of a given tree.
    References are:
    -- Weihs, C., Buschfeld, S. (2021a) "Combining Prediction and Interpretation in 
    Decision Trees (PrInDT) - a Linguistic Example" <arXiv:2103.02336>;
    -- Weihs, C., Buschfeld, S. (2021b) "NesPrInDT: Nested undersampling in PrInDT" 
    <arXiv:2103.14931>;
    -- Weihs, C., Buschfeld, S. (2021c) "Repeated undersampling in PrInDT (RePrInDT): Variation 
    in undersampling and prediction, and ranking of predictors in ensembles" <arXiv:2108.05129>.
	"""
	
	cran = "PrInDT" 

	version("1.0.1", md5="edc98fecf89c7cdf335624539e2a26cc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
