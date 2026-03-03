# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsc(RPackage):
	"""Effect Size Computation for Meta Analysis

	Implementation of the web-based 'Practical Meta-Analysis Effect Size
    Calculator' from David B. Wilson (<http://www.campbellcollaboration.org/escalc/html/EffectSizeCalculator-Home.php>)
    in R. Based on the input, the effect size can be returned as standardized mean 
    difference, Cohen's f, Hedges' g, Pearson's r or Fisher's
    transformation z, odds ratio or log odds, or eta squared effect size.
	"""
	
	homepage = "https://strengejacke.github.io/esc"
	cran = "esc" 

	version("0.5.1", md5="ca64b177c3f54973208f190488ca35d2")

	depends_on("r@3.2:", type=("build", "run"))
