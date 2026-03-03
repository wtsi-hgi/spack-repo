# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreatmentselection(RPackage):
	"""Evaluate Treatment Selection Biomarkers

	A suite of descriptive and inferential methods designed to evaluate one or more biomarkers for their ability to guide patient treatment recommendations.  Package includes functions to assess the calibration of risk models; and plot, evaluate, and compare markers. Please see the reference Janes H, Brown MD, Huang Y, et al. (2014) <doi:10.1515/ijb-2012-0052> for further details. 
	"""
	
	homepage = "http://rpubs.com/mdbrown/TreatmentSelection"
	cran = "TreatmentSelection" 

	version("2.1.1", md5="b26b6be5434df2aca9fe986ee3cd624f")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
