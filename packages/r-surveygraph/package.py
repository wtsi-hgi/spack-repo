# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveygraph(RPackage):
	"""Network Representations of Attitudes

	A tool for computing network representations of attitudes,
  extracted from tabular data such as sociological surveys. By treating
  a survey as a bipartite network, we measure the similarity between
  respondents and survey items to produce network edges. We do this in both a
  respondent network, as well as a survey item network. Used in combination
  with graph visualisation libraries, this technique helps practitioners in the
  social sciences identify network structure that may be present within a
  survey.
	"""
	
	homepage = "https://surveygraph.ie/"
	cran = "surveygraph" 

	version("0.1.1", md5="eea52c76bd8b342f58b0811d861c787e")

	depends_on("r@2.15.1:", type=("build", "run"))
