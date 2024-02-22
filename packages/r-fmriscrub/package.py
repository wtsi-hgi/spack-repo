# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmriscrub(RPackage):
	"""Scrubbing and Other Data Cleaning Routines for fMRI

	Data-driven fMRI denoising with projection scrubbing (Pham et al 
    (2022) <doi:10.1016/j.neuroimage.2023.119972>). Also includes routines for 
    DVARS (Derivatives VARianceS) (Afyouni and Nichols (2018) 
    <doi:10.1016/j.neuroimage.2017.12.098>), motion scrubbing (Power et al 
    (2012) <doi:10.1016/j.neuroimage.2011.10.018>), aCompCor (anatomical 
    Components Correction) (Muschelli et al (2014)
    <doi:10.1016/j.neuroimage.2014.03.028>), detrending, and nuisance
    regression. Projection scrubbing is also applicable to other
    outlier detection tasks involving high-dimensional data.
	"""
	
	homepage = "https://github.com/mandymejia/fMRIscrub"
	cran = "fMRIscrub" 

	version("0.14.5", md5="25b1ae916abfe85eef870313fd682a9d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cellwise", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fmritools@0.2.2:", type=("build", "run"))
	depends_on("r-pesel", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
