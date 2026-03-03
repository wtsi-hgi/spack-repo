# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioacoustics(RPackage):
	"""Analyse Audio Recordings and Automatically Extract Animal
Vocalizations

	Contains all the necessary tools to process audio recordings of
             various formats (e.g., WAV, WAC, MP3, ZC), filter noisy files, 
             display audio signals, detect and extract automatically acoustic
             features for further analysis such as classification.
	"""
	
	homepage = "https://github.com/wavx/bioacoustics/"
	cran = "bioacoustics" 

	version("0.2.8", md5="9ae1d01aa841f46acecf70b388124456")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tuner@1.3:", type=("build", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
	depends_on("cmake", type=("build", "link", "run"))
