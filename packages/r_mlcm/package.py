# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlcm(RPackage):
	"""Maximum Likelihood Conjoint Measurement

	Conjoint measurement is a psychophysical procedure in which stimulus pairs are presented that vary along 2 or more dimensions and the observer is required to compare the stimuli along one of them.  This package contains functions to estimate the contribution of the n scales to the judgment by a maximum likelihood method under several hypotheses of how the perceptual dimensions interact. Reference: Knoblauch & Maloney (2012) "Modeling Psychophysical Data in R". <doi:10.1007/978-1-4614-4475-6>.
	"""
	
	cran = "MLCM" 

	version("0.4.3", md5="ed317b02feb70a138d6643a44431373d")

	depends_on("r@3.5:", type=("build", "run"))
