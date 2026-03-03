# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsentropies(RPackage):
	"""Time Series Entropies

	Computes various entropies of given time series. This is the initial version that includes ApEn() and SampEn() functions for calculating approximate entropy and sample entropy. Approximate entropy was proposed by S.M. Pincus in "Approximate entropy as a measure of system complexity", Proceedings of the National Academy of Sciences of the United States of America, 88, 2297-2301 (March 1991). Sample entropy was proposed by J. S. Richman and J. R. Moorman in "Physiological time-series analysis using approximate entropy and sample entropy", American Journal of Physiology, Heart and Circulatory Physiology, 278, 2039-2049 (June 2000). This package also contains FastApEn() and FastSampEn() functions for calculating fast approximate entropy and fast sample entropy. These are newly designed very fast algorithms, resulting from the modification of the original algorithms. The calculated values of these entropies are not the same as the original ones, but the entropy trend of the analyzed time series determines equally reliably. Their main advantage is their speed, which is up to a thousand times higher. A scientific article describing their properties has been submitted to The Journal of Supercomputing and in present time it is waiting for the acceptance.
	"""
	
	cran = "TSEntropies" 

	version("0.9", md5="230731073397e53015f209773a44832b")

	depends_on("r@3.4:", type=("build", "run"))
