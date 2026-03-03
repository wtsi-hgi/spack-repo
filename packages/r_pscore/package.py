# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPscore(RPackage):
	"""Standardizing Physiological Composite Risk Endpoints

	Provides a number of functions to
  simplify and automate the scoring, comparison, and evaluation of
  different ways of creating composites of data.  It is particularly
  aimed at facilitating the creation of physiological composites of
  metabolic syndrome symptom score (MetSSS) and allostatic load (AL).
  Provides a wrapper to calculate the MetSSS on new data using the
  Healthy Hearts formula. 
	"""
	
	homepage = "https://score-project.org"
	cran = "pscore" 

	version("0.4.0", md5="8c3d23168a9c0a80c6d9086ac4efaee2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-jwileymisc@1.3:", type=("build", "run"))
