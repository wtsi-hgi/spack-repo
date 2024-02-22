# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtsa(RPackage):
	"""'Trial Sequential Analysis' for Error Control and Inference in
Sequential Meta-Analyses

	Frequentist sequential meta-analysis based on 
    'Trial Sequential Analysis' (TSA) in programmed in Java by the Copenhagen 
    Trial Unit (CTU). The primary function is the calculation of group 
    sequential designs for meta-analysis to be used for planning and analysis of
    both prospective and retrospective sequential meta-analyses to preserve 
    type-I-error control under sequential testing. 'RTSA' includes tools for 
    sample size and trial size calculation for meta-analysis and core 
    meta-analyses methods such as fixed-effect and random-effects models and
    forest plots. TSA is described in Wetterslev et. al (2008) 
    <doi:10.1016/j.jclinepi.2007.03.013>. The methods for deriving the
    group sequential designs are based on Jennison and Turnbull (1999,
    ISBN:9780849303166).
	"""
	
	homepage = "https://github.com/AnneLyng/RTSA"
	cran = "RTSA" 

	version("0.2.2", md5="be93ee1276707e40100ebd1f4f8645fe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
