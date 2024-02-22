# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBarulho(RPackage):
	"""Quantifying Habitat-Induced Acoustic Signal Degradation

	Intended to facilitate acoustic analysis of (animal) sound transmission experiments, which typically aim to quantify changes in signal structure when transmitted in a given habitat by broadcasting and re-recording animal sounds at increasing distances. The package offers a workflow with functions to prepare the data set for analysis as well as to calculate and visualize several degradation metrics, including blur ratio, signal-to-noise ratio, excess attenuation and envelope correlation among others (Dabelsteen et al 1993 <doi:10.1121/1.406682>).
	"""
	
	homepage = "https://github.com/maRce10/baRulho"
	cran = "baRulho" 

	version("1.0.6", md5="07cfc3faac09c7a85da3f6d4ffe49d66")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-warbler@1.1.27:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-fftw", type=("build", "run"))
