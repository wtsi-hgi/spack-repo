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
    and Sobel's test under the composite null hypothesis. Du, J., Zhou, X., Hao, W.,
    Liu, Y., Smith, J. A., & Mukherjee, B (2022) "Methods for Large-scale Single
    Mediator Hypothesis Testing: Possible Choices and Comparisons."
    arXiv preprint <arXiv:2203.13293>.
	"""
	
	homepage = "https://github.com/umich-cphds/medScan"
	cran = "medScan" 

	version("1.0.1", md5="b0a476eee4b121957cd0765983c8e5ab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hdmt", type=("build", "run"))
	depends_on("r-locfdr", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
