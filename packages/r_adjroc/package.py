# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdjroc(RPackage):
	"""Computing Sensitivity at a Fix Value of Specificity and Vice
Versa as Well as Bootstrap Metrics for ROC Curves

	For a binary classification the adjusted sensitivity and specificity 
             are measured for a given fixed threshold. If the threshold for either 
             sensitivity or specificity is not given, the crossing point between 
             the sensitivity and specificity curves are returned. For bootstrap 
             procedures, mean and CI bootstrap values of sensitivity, specificity, 
             crossing point between specificity and specificity as well as AUC 
             and AUCPR can be evaluated.
	"""
	
	homepage = "https://github.com/haghish/adjROC"
	cran = "adjROC" 

	version("0.3", md5="73539cfe19842c0b14fe3811b014d377")

	depends_on("r-rocit", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
