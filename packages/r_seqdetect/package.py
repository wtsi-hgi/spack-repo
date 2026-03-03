# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqdetect(RPackage):
	"""Sequence and Latent Process Detector

	Sequence detector in this package contains a specific automaton model that can be used to learn and detect data and process sequences.
    Automaton model in this package is capable of learning and tracing sequences. Automaton model can be found in Krleža, Vrdoljak, Brčić (2019) <doi:10.1109/ACCESS.2019.2955245>.
    This research has been partly supported under Competitiveness and Cohesion Operational Programme from the European Regional and Development Fund, as part of the Integrated Anti-Fraud System project no. KK.01.2.1.01.0041. This research has also been partly supported by the European Regional Development Fund under the grant KK.01.1.1.01.0009.
	"""
	
	cran = "SeqDetect" 

	version("1.0.7", md5="538ea1f6a935bf7b03442cf9e9e1da3c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-eventdatar", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
