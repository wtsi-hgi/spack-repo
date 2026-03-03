# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAta(RPackage):
	"""Automated Test Assembly

	Provides a collection of psychometric methods to process item metadata
 and use target assessment and measurement blueprint constraints to assemble a test form. Currently two automatic
 test assembly (ata) approaches are enabled. For example, the weighted (positive) deviations method, wdm(), proposed
 by Swanson and Stocking (1993) <doi:10.1177/014662169301700205> was implemented in its full specification allowing
 for both item selection as well as test form refinement. The linear constraint programming approach, atalp(), uses the 
 linear equation solver by Berkelaar et. al (2014) <http://lpsolve.sourceforge.net/5.5/>
 to enable a variety of approaches to select items.
	"""
	
	cran = "ata" 

	version("1.1.1", md5="810918efaa162a83e0844ee4007b9516")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
