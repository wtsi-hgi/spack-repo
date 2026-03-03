# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeewave(RPackage):
	"""Sound Analysis and Synthesis

	Functions for analysing, manipulating, displaying, editing and synthesizing time waves (particularly sound).  This package processes time analysis (oscillograms and envelopes), spectral content, resonance quality factor, entropy, cross correlation and autocorrelation, zero-crossing, dominant frequency, analytic signal, frequency coherence, 2D and 3D spectrograms and many other analyses. See Sueur et al. (2008) <doi:10.1080/09524622.2008.9753600> and Sueur (2018) <doi:10.1007/978-3-319-77647-7>.
	"""
	
	homepage = "https://rug.mnhn.fr/seewave/"
	cran = "seewave" 

	version("2.2.3", md5="c295faf9b8f61216b841ce1ceb087bcf")

	depends_on("r-tuner", type=("build", "run"))
	depends_on("libsndfile", type=("build", "link", "run"))
