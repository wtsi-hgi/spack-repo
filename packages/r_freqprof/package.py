# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreqprof(RPackage):
	"""Frequency Profiles Computing and Plotting

	Tools for generating an informative type of line graph, the frequency profile, 
    which allows single behaviors, multiple behaviors, or the specific behavioral patterns 
    of individual subjects to be graphed from occurrence/nonoccurrence behavioral data.
	"""
	
	homepage = "https://github.com/AIBRT/FreqProf"
	cran = "FreqProf" 

	version("0.0.1", md5="cae8574da059bc9bb7824901e144d4cf")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
