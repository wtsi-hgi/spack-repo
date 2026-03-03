# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlindrecalc(RPackage):
	"""Blinded Sample Size Recalculation

	Computation of key characteristics and plots for blinded sample size recalculation.
   Continuous as well as binary endpoints are supported in superiority and non-inferiority trials.
   See Baumann, Pilz, Kieser (2022) <doi:10.32614/RJ-2022-001> for a detailed description.
   The implemented methods include the approaches by
   Lu, K. (2019) <doi:10.1002/pst.1737>,
   Kieser, M. and Friede, T. (2000) <doi:10.1002/(SICI)1097-0258(20000415)19:7%3C901::AID-SIM405%3E3.0.CO;2-L>,
   Friede, T. and Kieser, M. (2004) <doi:10.1002/pst.140>, 
   Friede, T., Mitchell, C., Mueller-Veltern, G. (2007) <doi:10.1002/bimj.200610373>, and
   Friede, T. and Kieser, M. (2011) <doi:10.3414/ME09-01-0063>.
	"""
	
	homepage = "https://github.com/imbi-heidelberg/blindrecalc"
	cran = "blindrecalc" 

	version("1.0.1", md5="7ea99bae09cb9df33017eec383aac213")

	depends_on("r-rcpp", type=("build", "run"))
