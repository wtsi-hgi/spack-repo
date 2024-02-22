# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElochoice(RPackage):
	"""Preference Rating for Visual Stimuli Based on Elo Ratings

	Allows calculating global scores for characteristics of visual stimuli as assessed by human raters. Stimuli are presented as sequence of pairwise comparisons ('contests'), during each of which a rater expresses preference for one stimulus over the other (forced choice). The algorithm for calculating global scores is based on Elo rating, which updates individual scores after each single pairwise contest. Elo rating is widely used to rank chess players according to their performance. Its core feature is that dyadic contests with expected outcomes lead to smaller changes of participants' scores than outcomes that were unexpected. As such, Elo rating is an efficient tool to rate individual stimuli when a large number of such stimuli are paired against each other in the context of experiments where the goal is to rank stimuli according to some characteristic of interest. Clark et al (2018) <doi:10.1371/journal.pone.0190393> provide details.
	"""
	
	homepage = "https://github.com/gobbios/EloChoice"
	cran = "EloChoice" 

	version("0.29.4", md5="450d1b069583eb14253d3b7a2bb69c3b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
