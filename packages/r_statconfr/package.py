# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatconfr(RPackage):
	"""Models of Decision Confidence and Metacognition

	Provides fitting functions and other tools for decision confidence 
    and metacognition researchers, including meta-d´/d´, often considered to be 
    the gold standard to measure metacognitive efficiency.
    Also allows to fit several static models of decision making and confidence 
    to test the assumptions underlying meta-d´/d´ and which may serve as an 
    alternative when the assumptions of meta-d´/d´ do not hold. See also Rausch 
    et al. (2023) <doi:10.31234/osf.io/kdz34>.
	"""
	
	homepage = "https://github.com/ManuelRausch/StatConfR"
	cran = "statConfR" 

	version("0.0.1", md5="3f355791100cf274259fc074d221ec52")

	depends_on("r@4:", type=("build", "run"))
