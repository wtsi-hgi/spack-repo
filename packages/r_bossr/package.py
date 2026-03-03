# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBossr(RPackage):
	"""Biomarker Optimal Segmentation System

	The Biomarker Optimal Segmentation System R package, 'bossR', is designed for precision medicine, helping to identify individual traits using biomarkers. It focuses on determining the most effective cutoff value for a continuous biomarker, which is crucial for categorizing patients into two groups with distinctly different clinical outcomes. The package simultaneously finds the optimal cutoff from given candidate values and tests its significance. Simulation studies demonstrate that 'bossR' offers statistical power and false positive control non-inferior to the permutation approach (considered the gold standard in this field), while being hundreds of times faster. 
	"""
	
	cran = "bossR" 

	version("1.0.4", md5="18cced31a7c0dfbb660a993025f2cc13")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
