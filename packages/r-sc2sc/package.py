# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSc2sc(RPackage):
	"""Spatial Transfer of Statistics among Spanish Census Sections

	Transfers/imputes statistics among Spanish spatial polygons (census sections or postal code areas) from different moments in time (2001-2023) without need of spatial files, just linking statistics to the ID codes of the spatial units. 
    The data available in the census sections of a partition/division (cartography) into force in a moment of time is transferred to the census sections of another partition/division employing the geometric approach (also known as areal weighting or polygon overlay). 
    References: 
    Goerlich (2022) <doi:10.12842/WPIVIE_0322>.
    Pavía and Cantarino (2017a, b) <doi:10.1111/gean.12112>, <doi:10.1016/j.apgeog.2017.06.021>.
    Acknowledgements:
    The authors wish to thank Consellería de Educación, Universidades y Empleo, Generalitat Valenciana (grant AICO/2021/257) and Ministerio de Economía e Innovación (grant PID2021-128228NB-I00) for supporting this research.
	"""
	
	cran = "sc2sc" 

	version("0.0.1-12", md5="c322623fd9846e0f10ca8d40e8146fcd")

	depends_on("r@2.10:", type=("build", "run"))
