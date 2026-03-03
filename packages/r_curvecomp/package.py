# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurvecomp(RPackage):
	"""Multiple Curve Comparisons Using Parametric Bootstrap

	Performs multiple comparison procedures on curve observations among different treatment groups. The methods are applicable in a variety of situations (such as independent groups with equal or unequal sample sizes, or repeated measures) by using parametric bootstrap. References to these procedures can be found at Konietschke, Gel, and Brunner (2014) <doi:10.1090/conm/622/12431> and Westfall (2011) <doi:10.1080/10543406.2011.607751>.
	"""
	
	cran = "curvecomp" 

	version("0.1.0", md5="a5e7c47abfc1d17328d8d3b42f396dba")

	depends_on("r-multcomp@0.4.8:", type=("build", "run"))
