# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedscan(RPackage):
	"""Large Scale Single Mediator Hypothesis Testing

	A collection of methods for large scale single mediator hypothesis
    testing. The six included methods for testing the mediation effect are Sobel's
    test, Max P test, joint significance test under the composite null hypothesis,
    high dimensional mediation testing, divide-aggregate composite null test,
    and Sobel's test under the composite null hypothesis. Du et al (2023) 
    <doi:10.1002/gepi.22510>.
	"""
	
	homepage = "https://github.com/umich-cphds/medScan"
	cran = "medScan" 

	version("1.0.2", md5="a841eaab5c01da12d5020595c1ebbdda")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hdmt", type=("build", "run"))
	depends_on("r-locfdr", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
