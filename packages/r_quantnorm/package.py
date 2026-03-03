# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantnorm(RPackage):
	"""Mitigating the Adverse Impact of Batch Effects in Sample Pattern
Detection

	Modifies the distance matrix obtained from data with batch effects, so as to improve the performance of sample pattern detection, such as clustering, dimension reduction, and construction of networks between subjects. The method has been published in Bioinformatics (Fei et al, 2018, <doi:10.1093/bioinformatics/bty117>). Also available on 'GitHub' <https://github.com/tengfei-emory/QuantNorm>.
	"""
	
	cran = "QuantNorm" 

	version("1.0.5", md5="a882f41bbd5324329850891b1dc3cfc3")

	depends_on("r@3.3:", type=("build", "run"))
