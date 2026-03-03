# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewfocus(RPackage):
	"""True Discovery Guarantee by Combining Partial Closed Testings

	Closed testing has been proved powerful for true discovery guarantee. The computation of closed testing is, however, quite burdensome. A general way to reduce computational complexity is to combine partial closed testings for some prespecified feature sets of interest. Partial closed testings are performed at Bonferroni-corrected alpha level to guarantee the lower bounds for the number of true discoveries in prespecified sets are simultaneously valid. For any post hoc chosen sets of interest, coherence property is used to get the lower bound. In this package, we implement closed testing with globaltest to calculate the lower bound for number of true discoveries, see Ningning Xu et.al (2021) <arXiv:2001.01541> for detailed description. 
	"""
	
	cran = "newFocus" 

	version("1.1", md5="3e98085893094f05506b8f0463f5bc79")

	depends_on("r-ctgt", type=("build", "run"))
