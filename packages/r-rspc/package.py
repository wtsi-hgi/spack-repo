# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRspc(RPackage):
	"""Nelson Rules for Control Charts

	Implementation of Nelson rules for control charts in 'R'. The 'Rspc' implements some Statistical Process Control methods, namely Levey-Jennings type of I (individuals) chart, Shewhart C (count) chart and Nelson rules (as described in Montgomery, D. C. (2013) Introduction to statistical quality control. Hoboken, NJ: Wiley.). Typical workflow is taking the time series, specify the control limits, and list of Nelson rules you want to evaluate. There are several options how to modify the rules (one sided limits, numerical parameters of rules, etc.). Package is also capable of calculating the control limits from the data (so far only for i-chart and c-chart are implemented).
	"""
	
	cran = "Rspc" 

	version("1.2.2", md5="c300edbfe9ca39424c356bdd48e30432")

	depends_on("r@3.1:", type=("build", "run"))
