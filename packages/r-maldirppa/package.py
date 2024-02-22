# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaldirppa(RPackage):
	"""MALDI Mass Spectrometry Data Robust Pre-Processing and Analysis

	Provides methods for quality control and robust pre-processing and analysis of MALDI mass spectrometry data (Palarea-Albaladejo et al. (2018) <doi:10.1093/bioinformatics/btx628>).
	"""
	
	homepage = "https://github.com/Japal/MALDIrppa"
	cran = "MALDIrppa" 

	version("1.1.0-2", md5="959589f0a17920b99dd61f66c3ba00f0")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-maldiquant", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
