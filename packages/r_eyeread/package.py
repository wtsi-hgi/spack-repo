# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REyeread(RPackage):
	"""Prepare/Analyse Eye Tracking Data for Reading

	Functions to prepare and analyse eye tracking data of reading
  exercises. The functions allow some basic data preparations and code fixations 
  as first and second pass. First passes can be further devided into forward and 
  reading. The package further allows for aggregating fixation times per AOI or 
  per AOI and per type of pass (first forward, first rereading, second). These 
  methods are based on Hyönä, Lorch, and Rinck (2003) <doi:10.1016/B978-044451020-4/50018-9> 
  and Hyönä, and Lorch (2004) <doi:10.1016/j.learninstruc.2004.01.001>. It is 
  also possible to convert between metric length and visual degrees.
	"""
	
	homepage = "https://github.com/SanVerhavert/eyeRead"
	cran = "eyeRead" 

	version("0.0.4", md5="63a523e271dee3c435078ebc27ae99b7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
