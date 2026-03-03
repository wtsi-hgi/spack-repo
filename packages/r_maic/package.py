# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaic(RPackage):
	"""Matching-Adjusted Indirect Comparison

	A generalised workflow for generation of subject weights to be 
    used in Matching-Adjusted Indirect Comparison (MAIC) per Signorovitch et 
    al. (2012) <doi:10.1016/j.jval.2012.05.004>, Signorovitch et al (2010) 
    <doi:10.2165/11538370-000000000-00000>. In MAIC, unbiased 
    comparison between outcomes of two trials is facilitated by weighting the
    subject-level outcomes of one trial with weights derived such that the 
    weighted aggregate measures of the prognostic or effect modifying variables 
    are equal to those of the sample in the comparator trial. The functions and
    classes included in this package wrap and abstract the process demonstrated
    in the UK National Institute for Health and Care Excellence Decision 
    Support Unit (NICE DSU)'s example (Phillippo et al, (2016) [see URL]),
    providing a repeatable and easily specifiable workflow for producing 
    multiple comparison variable sets against a variety of target studies, with
    preprocessing for a number of aggregate target forms (e.g. mean, median, 
    domain limits).
	"""
	
	homepage = "https://github.com/heorltd/maic"
	cran = "maic" 

	version("0.1.4", md5="3df1f1cea1872d92138ffb0b2de8f1e1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
