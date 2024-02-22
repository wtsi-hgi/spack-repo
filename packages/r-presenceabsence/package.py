# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresenceabsence(RPackage):
	"""Presence-Absence Model Evaluation

	Provides a set of functions useful when evaluating the results of presence-absence models. Package includes functions for calculating threshold dependent measures such as confusion matrices, pcc, sensitivity, specificity, and Kappa, and produces plots of each measure as the threshold is varied. It will calculate optimal threshold choice according to a choice of optimization criteria. It also includes functions to plot the threshold independent ROC curves along with the associated AUC (area under the curve).
	"""
	
	cran = "PresenceAbsence" 

	version("1.1.11", md5="962aecac4b8eec3ba093172e6ec2761f")

	depends_on("r@2.2:", type=("build", "run"))
