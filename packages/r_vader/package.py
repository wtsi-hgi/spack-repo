# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVader(RPackage):
	"""Valence Aware Dictionary and sEntiment Reasoner (VADER)

	A lexicon and rule-based sentiment analysis tool that is specifically 
    attuned to sentiments expressed in social media, and works well on texts from other 
    domains. Hutto & Gilbert (2014) <https://www.aaai.org/ocs/index.php/ICWSM/ICWSM14/paper/view/8109/8122>. 
	"""
	
	cran = "vader" 

	version("0.2.1", md5="5465636c7c352a61b026803bc706146c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
