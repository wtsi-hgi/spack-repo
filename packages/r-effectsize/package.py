# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffectsize(RPackage):
	"""Indices of Effect Size

	Provide utilities to work with indices of effect size for a wide 
    variety of models and hypothesis tests (see list of supported models using 
    the function 'insight::supported_models()'), allowing computation of and 
    conversion between indices such as Cohen's d, r, odds, etc.
    References: Ben-Shachar et al. (2020) <doi:10.21105/joss.02815>.
	"""
	
	homepage = "https://easystats.github.io/effectsize/"
	cran = "effectsize" 

	version("0.8.7", md5="abe197ef35f15d4ff62803f49a2c4f2c")
	version("0.8.6", md5="24f114041cd5ca301e46706a8fd53274")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13.2:", type=("build", "run"))
	depends_on("r-insight@0.19.9:", type=("build", "run"))
	depends_on("r-parameters@0.21.6:", type=("build", "run"))
	depends_on("r-performance@0.11:", type=("build", "run"))
	depends_on("r-datawizard@0.9.1:", type=("build", "run"))
