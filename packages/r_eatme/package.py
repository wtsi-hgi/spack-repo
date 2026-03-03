# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REatme(RPackage):
	"""Exponentially Weighted Moving Average with Adjustments to
Measurement Error

	The univariate statistical quality control tool aims to address measurement error effects when constructing exponentially weighted moving average p control charts. The method primarily focuses on binary random variables, but it can be applied to any continuous random variables by using sign statistic to transform them to discrete ones. With the correction of measurement error effects, we can obtain the corrected control limits of exponentially weighted moving average p control chart and reasonably adjusted exponentially weighted moving average p control charts. The methods in this package can be found in some relevant references, such as Chen and Yang (2022) <arXiv: 2203.03384>; Yang et al. (2011) <doi: 10.1016/j.eswa.2010.11.044>; Yang and Arnold (2014) <doi: 10.1155/2014/238719>; Yang (2016) <doi: 10.1080/03610918.2013.763980> and Yang and Arnold (2016) <doi: 10.1080/00949655.2015.1125901>.
	"""
	
	cran = "EATME" 

	version("0.1.0", md5="5b09c59ca8f6e5148ed12bc14d49591a")

	depends_on("r-qcr", type=("build", "run"))
