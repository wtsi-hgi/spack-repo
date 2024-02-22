# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeanr(RPackage):
	"""Sentiment Analysis Scorer

	Sentiment analysis is a popular technique in text mining that
    attempts to determine the emotional state of some text. We provide a new
    implementation of a common method for computing sentiment, whereby words are
    scored as positive or negative according to a dictionary lookup. Then the
    sum of those scores is returned for the document. We use the 'Hu' and 'Liu'
    sentiment dictionary ('Hu' and 'Liu', 2004) <doi:10.1145/1014052.1014073>
    for determining sentiment. The scoring function is 'vectorized' by document,
    and scores for multiple documents are computed in parallel via 'OpenMP'.
	"""
	
	homepage = "https://github.com/wrathematics/meanr"
	cran = "meanr" 

	version("0.1-6", md5="03b6b6e321dbbeb60a681aca4f82e1ea")

	depends_on("r@3:", type=("build", "run"))
