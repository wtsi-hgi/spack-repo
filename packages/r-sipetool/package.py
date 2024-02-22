# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSipetool(RPackage):
	"""SIFT-MS and CPET Data Processor

	Processor for selected ion flow tube mass spectrometer
            (SIFT-MS) output file from breath analysis. It allows the filtering of the SIFT output file (i.e., variation
            over time of the target analyte concentration) and the following
            analysis for the determination of: maximum, average, and standard deviation
            value of target concentration measured at each exhalation, and the
            respiratory rate over the measurement. Additionally, it is possible to
            align the SIFT-MS data with other on-line techniques such as 
            cardio pulmonary exercise test (CPET) for a comprehensive 
            characterization of breath samples.
	"""
	
	cran = "SIPETool" 

	version("0.1.0", md5="d18e1901f4380627384298f39f3f53d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-convolutioner", type=("build", "run"))
