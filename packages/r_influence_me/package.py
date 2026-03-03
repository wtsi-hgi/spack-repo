# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfluenceMe(RPackage):
	"""Tools for Detecting Influential Data in Mixed Effects Models

	Provides a collection of tools for
        detecting influential cases in generalized mixed effects
        models. It analyses models that were estimated using 'lme4'. The
        basic rationale behind identifying influential data is that
        when single units are omitted from the data, models
        based on these data should not produce substantially different
        estimates. To standardize the assessment of how influential a
        (single group of) observation(s) is, several measures of
        influence are common practice, such as Cook's Distance. 
        In addition, we provide a measure of percentage change of the fixed point 
        estimates and a simple procedure to detect changing levels of significance.
	"""
	
	homepage = "http://www.rensenieuwenhuis.nl/r-project/influenceme/"
	cran = "influence.ME" 

	version("0.9-9", md5="83b6b2177557b8c1e7ed5b5f5cad6dbb")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
	depends_on("r-matrix@1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
