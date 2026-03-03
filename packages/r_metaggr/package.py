# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaggr(RPackage):
	"""Calculate the Knowledge-Weighted Estimate

	
    According to a phenomenon known as "the wisdom of the crowds," 
    combining point estimates from multiple judges often provides a 
    more accurate aggregate estimate than using a point estimate from
    a single judge. However, if the judges use shared information in 
    their estimates, the simple average will over-emphasize this common
    component at the expense of the judges’ private information. 
    Asa Palley & Ville Satopää (2021) "Boosting the Wisdom of Crowds
    Within a Single Judgment Problem: Selective Averaging Based on Peer Predictions"
    <https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=3504286> proposes
    a procedure for calculating a weighted average of the judges’ individual
    estimates such that resulting aggregate estimate appropriately combines
    the judges' collective information within a single estimation problem. 
    The authors use both simulation and data from six experimental studies
    to illustrate that the weighting procedure outperforms existing averaging-like
    methods, such as the equally weighted average, trimmed average, and median.
    This aggregate estimate -- know as "the knowledge-weighted estimate" --
    inputs a) judges' estimates of a continuous outcome (E) and 
    b) predictions of others' average estimate of this outcome (P).  
    In this R-package, the function knowledge_weighted_estimate(E,P) 
    implements the knowledge-weighted estimate. Its use is illustrated
    with a simple stylized example and on real-world experimental data. 
	"""
	
	cran = "metaggR" 

	version("0.3.0", md5="9471e4615ec89f59d2919cfe4aa7a29f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
