# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemova(RPackage):
	"""DEvelopment (of Multi-Linear QSPR/QSAR) MOdels VAlidated using
Test Set

	Tool for the development of multi-linear QSPR/QSAR models (Quantitative structure-property/activity relationship). Theses models are used in chemistry, biology and pharmacy to find a relationship between the structure of a molecule and its property (such as activity, toxicology but also physical properties). The various functions of this package allows: selection of descriptors based of variances, intercorrelation and user expertise; selection of the best multi-linear regression in terms of correlation and robustness; methods of internal validation (Leave-One-Out, Leave-Many-Out, Y-scrambling) and external using test sets.
	"""
	
	cran = "DEMOVA" 

	version("1.0", md5="9b9245499cd57310ddda29672a79e0b6")

	depends_on("r-leaps", type=("build", "run"))
