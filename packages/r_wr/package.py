# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWr(RPackage):
	"""Win Ratio Analysis of Composite Time-to-Event Outcomes

	Implements various win ratio methodologies for composite endpoints of death and 
  non-fatal events, including the (stratified) proportional win-fractions (PW) regression models 
  (Mao and Wang, 2020 <doi:10.1111/biom.13382>), (stratified) two-sample tests with possibly 
  recurrent nonfatal event, and sample size calculation for standard win ratio test (Mao et al., 
  2021 <doi:10.1111/biom.13501>).
	"""
	
	homepage = "https://sites.google.com/view/lmaowisc/"
	cran = "WR" 

	version("1.0", md5="4630c68eb980ded5eabd312c22456a14")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-gumbel", type=("build", "run"))
