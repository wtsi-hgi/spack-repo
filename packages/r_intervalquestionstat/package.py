# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntervalquestionstat(RPackage):
	"""Tools to Deal with Interval-Valued Responses in Questionnaires

	A user-friendly toolbox for doing the statistical analysis of
  interval-valued responses in questionnaires measuring intrinsically
  imprecise human attributes or features (attitudes, perceptions, opinions,
  feelings, etc.). In particular, this package provides S4 classes, methods,
  and functions in order to compute basic arithmetic and statistical operations
  with interval-valued data; prepare customized plots; associate each
  interval-valued response to its equivalent Likert-type and visual analogue
  scales answers through the minimum theta-distance and the mid-point criteria;
  analyze the reliability of respondents' answers from the internal consistency
  point of view by means of Cronbach's alpha coefficient; and simulate
  interval-valued responses in this type of questionnaires. The package also
  incorporates some real-life data that can be used to illustrate its working
  with several non-trivial reproducible examples. The methodology used in this
  package is based in many theoretical and applied publications from
  SMIRE+CoDiRE (Statistical Methods with Imprecise Random Elements and
  Comparison of Distributions of Random Elements) Research Group
  (<https://bellman.ciencias.uniovi.es/smire+codire/>)
  from the University of Oviedo (Spain).
	"""
	
	homepage = "https://github.com/garciagarjose/IntervalQuestionStat/"
	cran = "IntervalQuestionStat" 

	version("0.2.0", md5="8a7099043b0a9e7593ac1975df604d58")

	depends_on("r@3.5:", type=("build", "run"))
