# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWavesampling(RPackage):
	"""Weakly Associated Vectors (WAVE) Sampling

	Spatial data are generally auto-correlated, meaning that if two 
  units selected are close to each other, then it is likely that they share the
  same properties. For this reason, when sampling in the population it is often
  needed that the sample is well spread over space. A new method to draw a sample
  from a population with spatial coordinates is proposed. This method is called
  wave (Weakly Associated Vectors) sampling. It uses the less correlated vector
  to a spatial weights matrix to update the inclusion probabilities vector
  into a sample. For more details see Raphaël Jauslin and Yves Tillé (2019) <doi:10.1007/s13253-020-00407-1>.
	"""
	
	homepage = "https://github.com/RJauslin/WaveSampling"
	cran = "WaveSampling" 

	version("0.1.3", md5="6ff4635ee6ced996604ea60e8f97b3e9")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
