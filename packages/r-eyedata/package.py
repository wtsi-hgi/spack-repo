# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REyedata(RPackage):
	"""Open Source Ophthalmic Data Sets Curated for R

	Open source data allows for reproducible research and helps advance
    our knowledge. The purpose of this package is to collate open source 
    ophthalmic data sets curated for direct use. This is real life data of 
    people with intravitreal injections with anti-vascular endothelial growth
    factor (anti-VEGF), due to age-related macular degeneration or diabetic 
    macular edema. Associated publications of the data sets: 
    Fu et al. (2020) <doi:10.1001/jamaophthalmol.2020.5044>, 
    Moraes et al (2020) <doi:10.1016/j.ophtha.2020.09.025>,
    Fasler et al. (2019) <doi:10.1136/bmjopen-2018-027441>, 
    Arpa et al. (2020) <doi:10.1136/bjophthalmol-2020-317161>,
    Kern et al. 2020, <doi:10.1038/s41433-020-1048-0>.
	"""
	
	homepage = "https://github.com/tjebo/eyedata"
	cran = "eyedata" 

	version("0.1.0", md5="08aae00ed9519056267c54d83c9d19a5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
