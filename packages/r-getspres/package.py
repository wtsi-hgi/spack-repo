# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetspres(RPackage):
	"""SPRE Statistics for Exploring Heterogeneity in Meta-Analysis

	An implementation of SPRE (standardised predicted random-effects)
    statistics in R to explore heterogeneity in genetic association meta-
    analyses, as described by Magosi et al. (2019) 
    <doi:10.1093/bioinformatics/btz590>. SPRE statistics are precision 
    weighted residuals that indicate the direction and extent with which 
    individual study-effects in a meta-analysis deviate from the average 
    genetic effect. Overly influential positive outliers have the potential 
    to inflate average genetic effects in a meta-analysis whilst negative 
    outliers might lower or change the direction of effect. See the 'getspres' 
    website for documentation and examples 
    <https://magosil86.github.io/getspres/>.
	"""
	
	homepage = "https://magosil86.github.io/getspres/"
	cran = "getspres" 

	version("0.2.0", md5="3e905ca206c203f2ec371a5aa6aa29fa")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-metafor@1.9.6:", type=("build", "run"))
	depends_on("r-dplyr@0.4.1:", type=("build", "run"))
	depends_on("r-plotrix@3.5.12:", type=("build", "run"))
	depends_on("r-colorspace@1.2.6:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-colorramps@2.3:", type=("build", "run"))
