# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActcr(RPackage):
	"""Extract Circadian Rhythms Metrics from Actigraphy Data

	Circadian rhythms are rhythms that oscillate about every 24 h, which has been observed in multiple physiological processes including core body temperature, hormone secretion, heart rate, blood pressure, and many others. Measuring circadian rhythm with wearables is based on a principle that there is increased movement during wake periods and reduced movement during sleep periods, and has been shown to be reliable and valid. This package can be used to extract nonparametric circadian metrics like intradaily variability (IV), interdaily stability (IS), and relative amplitude (RA); and parametric cosinor model and extended cosinor model coefficient. Details can be found in Junrui Di et al (2019) <doi:10.1007/s12561-019-09236-4>.
	"""
	
	homepage = "https://github.com/junruidi/ActCR"
	cran = "ActCR" 

	version("0.3.0", md5="ed3de802693ece5f8ccef386df638055")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-cosinor", type=("build", "run"))
	depends_on("r-cosinor2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
