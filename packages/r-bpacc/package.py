# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpacc(RPackage):
	"""Blood Pressure Device Accuracy Evaluation: Statistical
Considerations

	A comprehensive statistical analysis of the accuracy of blood
         pressure devices based on the method of AAMI/ANSI SP10 standards
         developed by the AAMI Sphygmomanometer Committee for indirect
         measurement of blood pressure, incorporated into IS0 81060-2. The 
         'bpAcc' package gives the exact probability 'of accepting a device D'
         derived from the join distribution of the sample standard deviation
         and a non-linear transformation of the sample mean for a specified
         sample size introduced by Chandel et al. (2023) and by the Association
         for the Advancement of Medical Instrumentation (2003, ISBN:1-57020-183-8).
	"""
	
	cran = "bpAcc" 

	version("0.0-2", md5="cab4bbc4e5da7d598096c96b55a50992")

	depends_on("r@4.2:", type=("build", "run"))
