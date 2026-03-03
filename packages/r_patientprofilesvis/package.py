# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatientprofilesvis(RPackage):
	"""Visualization of Patient Profiles

	Creation of patient profile visualizations for
  exploration, diagnostic or monitoring purposes during a clinical trial.
  These static visualizations display a patient-specific overview
  of the evolution during the trial time frame of 
  parameters of interest (as laboratory, ECG, vital signs),
  presence of adverse events, exposure to a treatment; 
  associated with metadata patient information, 
  as demography, concomitant medication.
  The visualizations can be tailored for specific domain(s) or endpoint(s) of interest.
  Visualizations are exported into patient profile report(s)
  or can be embedded in custom report(s).
	"""
	
	homepage = "https://github.com/openanalytics/patientProfilesVis"
	cran = "patientProfilesVis" 

	version("2.0.7", md5="b8de518d693870f7c3d2455419150346")
	version("2.0.6", md5="93e8c02e893e0a399c12365f47acbd11")

	depends_on("r-clinutils", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("cairo", type=("build", "link", "run"))
