# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeltaccd(RPackage):
	"""Quantify Rhythmic Gene Co-Expression Relative to a Reference

	Infer progression of circadian rhythms in transcriptome data in
  which samples are not labeled with time of day and coverage of the circadian
  cycle may be incomplete. See Shilts et al. (2018) <doi:10.7717/peerj.4327>.
	"""
	
	homepage = "https://deltaccd.hugheylab.org"
	cran = "deltaccd" 

	version("1.0.2", md5="6f24b04edddd423d762101705a66f9fb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dorng@1.6.6:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-scales@0.5:", type=("build", "run"))
	depends_on("r-statmod@1.4.30:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
