# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausaldata(RPackage):
	"""Example Data Sets for Causal Inference Textbooks

	Example data sets to run the example
    problems from causal inference textbooks. Currently, contains data
    sets for Huntington-Klein, Nick (2021) "The Effect" <https://theeffectbook.net>,
    Cunningham, Scott (2021, ISBN-13: 978-0-300-25168-5) "Causal Inference: The Mixtape", 
    and Hernán, Miguel and James Robins (2020) "Causal Inference: What If" 
    <https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/>.
	"""
	
	homepage = "https://github.com/NickCH-K/causaldata"
	cran = "causaldata" 

	version("0.1.3", md5="e10355e03c729c7a0b2e013e0df18603")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
