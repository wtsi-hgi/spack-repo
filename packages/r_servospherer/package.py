# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RServospherer(RPackage):
	"""Analyze Data Generated from Syntech Servosphere Trials

	Functions that facilitate and speed up the analysis of data
    produced by a Syntech servosphere <http://www.ockenfels-syntech.com/products/locomotion-compensation/>,
    which is equipment for studying the movement behavior of arthropods.
    This package is designed to make working with data produced from a 
    servosphere easy for someone new to or unfamiliar with R. The functions
    provided in this package fall into three broad-use categories: functions for
    cleaning raw data produced by the servosphere software, functions for
    deriving movement variables based on position data, and functions for 
    summarizing movement variables for easier analysis. These functions are
    built with functions from the tidyverse package to work efficiently, as a
    single servosphere file may consist of hundreds of thousands of rows of data
    and a user may wish to analyze hundreds of files at a time. Many of the 
    movement variables derivable through this package are described in the 
    following papers:
    Otálora-Luna, Fernando; Dickens, Joseph C. (2011) <doi:10.1371/journal.pone.0020990>
    Party, Virginie; Hanot, Christophe; Busser, Daniela Schmidt; Rochat, Didier; Renou, Michel (2013) <doi:10.1371/journal.pone.0052897>
    Bell, William J.; Kramer, Ernest (1980) <doi:10.1007/BF01402908>
    Becher, Paul G; Guerin, Patrick M. (2009) <doi:10.1016/j.jinsphys.2009.01.006>.
	"""
	
	homepage = "http://github.com/wittja01/servosphereR"
	cran = "servosphereR" 

	version("0.1.1", md5="c3fdb71e645e136b55edfd9acd53cbbe")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr@0.2:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
