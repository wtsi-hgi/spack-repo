# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocket(RPackage):
	"""Simple and Fast ROC Curves

	A set of functions for receiver operating characteristic (ROC) curve 
    estimation and area under the curve (AUC) calculation.
    All functions are designed to work with aggregated data; 
    nevertheless, they can also handle raw samples. 
    In 'ROCket', we distinguish two types of ROC curve representations:
    1) parametric curves - the true positive rate (TPR) and the false positive rate (FPR) 
    are functions of a parameter (the score),
    2) functions - TPR is a function of FPR.
    There are several ROC curve estimation methods available. An introduction to 
    the mathematical background of the implemented methods (and much more) can be found in 
    de Zea Bermudez, Gonçalves, Oliveira & Subtil (2014) <https://www.ine.pt/revstat/pdf/rs140101.pdf> 
    and Cai & Pepe (2004) <doi:10.1111/j.0006-341X.2004.00200.x>.
	"""
	
	homepage = "https://github.com/da-zar/ROCket"
	cran = "ROCket" 

	version("1.0.1", md5="4027ad9387c8bcb035007a3e2ba6ebcf")

	depends_on("r-data-table@1.13:", type=("build", "run"))
