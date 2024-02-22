# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpringpheno(RPackage):
	"""Spring Phenological Indices

	Computes the extended spring indices (SI-x) and false spring 
    exposure indices (FSEI). The SI-x indices are standard indices used for 
    analysis in spring phenology studies. In addition, the FSEI is also from 
    research on the climatology of false springs and adjusted to include an 
    early and late false spring exposure index. The indices  include the 
    first leaf index, first bloom index, and false spring exposure indices, 
    along with all calculations for all functions needed to calculate 
    each index. The main function returns all indices, but each function can 
    also be run separately. 
    Allstadt et al. (2015) <doi: 10.1088/1748-9326/10/10/104008> 
    Ault et al. (2015) <doi: 10.1016/j.cageo.2015.06.015> 
    Peterson and Abatzoglou (2014) <doi: 10.1002/2014GL059266>
    Schwarz et al. (2006) <doi: 10.1111/j.1365-2486.2005.01097.x> 
    Schwarz et al. (2013) <doi: 10.1002/joc.3625>. 
	"""
	
	cran = "springpheno" 

	version("0.5.0", md5="38dc44cb27c99835c69fc44b1a45a503")

	depends_on("r@4.1:", type=("build", "run"))
