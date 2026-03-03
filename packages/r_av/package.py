# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAv(RPackage):
	"""Working with Audio and Video in R

	Bindings to 'FFmpeg' <http://www.ffmpeg.org/> AV library for working with 
    audio and video in R. Generates high quality video from images or R graphics with 
    custom audio. Also offers high performance tools for reading raw audio, creating
    'spectrograms', and converting between countless audio / video formats. This package 
    interfaces directly to the C API and does not require any command line utilities.
	"""
	
	homepage = "https://ropensci.r-universe.dev/av"
	cran = "av" 

	version("0.9.0", md5="3a990a185d9fee9b5d520d0598fefc2f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("ffmpeg", type=("build", "link", "run"))
