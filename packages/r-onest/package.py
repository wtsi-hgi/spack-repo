# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnest(RPackage):
	"""Observers Needed to Evaluate Subjective Tests

	
    This ONEST software implements the method of assessing the pathologist agreement in reading PD-L1 assays (Reisenbichler et al. (2020 <doi:10.1038/s41379-020-0544-x>)), to determine the minimum number of evaluators needed to estimate agreement involving a large number of raters. Input to the program should be binary(1/0) pathology data, where “0” may stand for negative and “1” for positive. Additional examples were given using the data from Rimm et al. (2017 <doi:10.1001/jamaoncol.2017.0013>). 
	"""
	
	homepage = "https://github.com/hangangtrue/ONEST"
	cran = "ONEST" 

	version("0.1.0", md5="1f8af421aa5e3299001e6ec890dd8c1f")

	depends_on("r@3.5:", type=("build", "run"))
