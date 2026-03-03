# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBraggr(RPackage):
	"""Calculate the Revealed Aggregator of Probability Predictions

	
    Forecasters predicting the chances of a future event may disagree due to
    differing evidence or noise. To harness the collective evidence of the crowd, 
    Ville Satopää (2021) "Regularized Aggregation of One-off Probability Predictions"
    <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3769945> proposes a Bayesian
    aggregator that is regularized by analyzing the forecasters' disagreement and ascribing 
    over-dispersion to noise. This aggregator requires no user intervention and can be computed
    efficiently even for a large numbers of predictions. The author evaluates
    the aggregator on subjective probability predictions collected during
    a four-year forecasting tournament sponsored by the US intelligence community.
    The aggregator improves the accuracy of simple averaging by around 20% and
    other state-of-the-art aggregators by 10-25%. The advantage stems almost
    exclusively from improved calibration. This aggregator -- know as "the revealed
    aggregator" -- inputs a) forecasters' probability predictions (p) of a future binary event
    and b) the forecasters' common prior (p0) of the future event. In this R-package,
    the function sample_aggregator(p,p0,...) allows the user to calculate the revealed
    aggregator. Its use is illustrated with a simple example. 
	"""
	
	cran = "braggR" 

	version("0.1.1", md5="73c16de2301e4cbfb1a7e45fc700ddc9")

	depends_on("r-rcpp", type=("build", "run"))
