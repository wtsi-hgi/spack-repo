# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonitos(RPackage):
	"""Monitoring Overall Survival in Pivotal Trials in Indolent
Cancers

	These guidelines are meant to provide a pragmatic, yet rigorous, help to drug developers and decision makers, since they are shaped by three fundamental ingredients: the clinically determined margin of detriment on OS that is unacceptably high (delta null); the benefit on OS that is plausible given the mechanism of action of the novel intervention (delta alt); and the quantity of information (i.e. survival events) it is feasible to accrue given the clinical and drug development setting. The proposed guidelines facilitate transparent discussions between stakeholders focusing on the risks of erroneous decisions and what might be an acceptable trade-off between power and the false positive error rate. 
	"""
	
	cran = "monitOS" 

	version("0.1.3", md5="618c8c861b07cdf8e3db893a9c5f6f3e")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
