# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZeitgebr(RPackage):
	"""Analysis of Circadian Behaviours

	Use behavioural variables to compute period, rhythmicity and other circadian parameters.
  Methods include computation of chi square periodograms (Sokolove and Bushell (1978) <DOI:10.1016/0022-5193(78)90022-X>),
  Lomb-Scargle periodograms (Lomb (1976) <DOI:10.1007/BF00648343>, Scargle (1982) <DOI:10.1086/160554>, Ruf (1999) <DOI:10.1076/brhm.30.2.178.1422>),
  and autocorrelation-based periodograms.
	"""
	
	homepage = "https://github.com/rethomics/zeitgebr"
	cran = "zeitgebr" 

	version("0.3.5", md5="f28e683af65d1ba5c6959d2909331bc6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-behavr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lomb", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-waveletcomp", type=("build", "run"))
