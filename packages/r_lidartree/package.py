# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLidartree(RPackage):
	"""Forest Analysis with Airborne Laser Scanning (LiDAR) Data

	Provides functions for forest analysis using airborne laser scanning (LiDAR remote sensing) data: 
    tree detection (method 1 in Eysn et al. (2015) <doi:10.3390/f6051721>) and segmentation; 
    forest parameters estimation and mapping with the area-based approach. It includes complementary steps for forest mapping: 
    co-registration of field plots with LiDAR data (Monnet and Mermin (2014) <doi:10.3390/f5092307>); 
    extraction of both physical (gaps, edges, trees) and statistical features from LiDAR data useful 
    for e.g. habitat suitability modeling (Glad et al. (2020) <doi:10.1002/rse2.117>) and forest maturity mapping (Fuhr et al. (2022) <doi:10.1002/rse2.274>); 
    model calibration with ground reference, and maps export. 
	"""
	
	homepage = "https://gitlab.irstea.fr/jean-matthieu.monnet/lidaRtRee"
	cran = "lidaRtRee" 

	version("4.0.5", md5="6a4de456ebf5e836add0e7602a3b7afa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-gvlma", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-reldist", type=("build", "run"))
	depends_on("r-lidr@4:", type=("build", "run"))
