# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrtopdownfrag(RPackage):
	"""Internal Fragment Identification from Top-Down Mass Spectrometry

	Top-Down mass spectrometry aims to identify entire proteins as well as their (post-translational) modifications or ions bound (eg Chen et al (2018) <doi:10.1021/acs.analchem.7b04747>). 
    The pattern of internal fragments (Haverland et al (2017) <doi:10.1007/s13361-017-1635-x>) may reveal important information about the original structure of the proteins studied 
    (Skinner et al (2018) <doi:10.1038/nchembio.2515> and Li et al (2018) <doi:10.1038/nchem.2908>). 
    However, the number of possible internal fragments gets huge with longer proteins and subsequent identification of internal fragments remains challenging, 
    in particular since the the accuracy of measurements with current mass spectrometers represents a limiting factor.   
    This package attempts to deal with the complexity of internal fragments and allows identification of terminal and internal fragments from deconvoluted mass-spectrometry data. 
	"""
	
	cran = "wrTopDownFrag" 

	version("1.0.2", md5="e862211c621d5af58550d28ab2e80cdf")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-wrmisc", type=("build", "run"))
	depends_on("r-wrproteo", type=("build", "run"))
