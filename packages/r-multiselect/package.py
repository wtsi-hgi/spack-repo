# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiselect(RPackage):
	"""Selecting Combinations of Predictors by Leveraging Multiple AUCs
for an Ordered Multilevel Outcome

	Uses multiple AUCs to select a combination of predictors when the outcome has multiple (ordered) levels and the focus is discriminating one particular level from the others. This method is most naturally applied to settings where the outcome has three levels. (Meisner, A, Parikh, CR, and Kerr, KF (2017) <http://biostats.bepress.com/uwbiostat/paper423/>.) 
	"""
	
	cran = "multiselect" 

	version("0.1.0", md5="9205ad29307d9db8af351fec1397dc59")

	depends_on("r-hmisc", type=("build", "run"))
