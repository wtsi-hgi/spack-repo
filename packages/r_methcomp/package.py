# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethcomp(RPackage):
	"""Analysis of Agreement in Method Comparison Studies

	Methods (standard and advanced) for analysis of agreement between measurement methods. These cover Bland-Altman plots, Deming regression, Lin's Total deviation index, and difference-on-average regression. See Carstensen B. (2010) "Comparing Clinical Measurement Methods: A Practical Guide (Statistics in Practice)" <doi:10.1002/9780470683019> for more information.
	"""
	
	homepage = "http://BendixCarstensen.com/MethComp/"
	cran = "MethComp" 

	version("1.30.0", md5="06fd0063f917b67e3e769a295689a10c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
