# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowthpheno(RPackage):
	"""Functional Analysis of Phenotypic Growth Data to Smooth and
Extract Traits

	Assists in the plotting and functional smoothing of traits 
    measured over time and the extraction of features from these traits, 
    implementing the SET (Smoothing and Extraction of Traits) method 
    described in Brien et al. (2020) Plant Methods, 16. Smoothing of 
    growth trends for individual plants using natural cubic smoothing 
    splines or P-splines is available for removing transient effects and 
    segmented smoothing is available to deal with discontinuities in 
    growth trends. There are graphical tools for assessing the adequacy 
    of trait smoothing, both when using this and other packages, such as 
    those that fit nonlinear growth models. A range of per-unit (plant, 
    pot, plot) growth traits or features can be extracted from the 
    data, including single time points, interval growth rates and other 
    growth statistics, such as maximum growth or days to maximum growth. 
    The package also has tools adapted to inputting data from 
    high-throughput phenotyping facilities, such from a Lemna-Tec 
    Scananalyzer 3D (see <https://www.youtube.com/watch?v=MRAF_mAEa7E/> 
    for more information). The package 'growthPheno' can also be 
    installed from <http://chris.brien.name/rpackages/>.
	"""
	
	homepage = "http://chris.brien.name/"
	cran = "growthPheno" 

	version("2.1.24", md5="c398ef449a8394e4133631f361817db1")
	version("2.1.23", md5="88a845d8baa7b302b9719a59304b97f9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dae", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-jops", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
