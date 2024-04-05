# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrt(RPackage):
	"""Read Subtitle Files as Tabular Data

	Read 'SubRip' <https://sourceforge.net/projects/subrip/>
    subtitle files as data frames for easy text analysis or manipulation.
    Easily shift numeric timings and export subtitles back into valid
    'SubRip' timestamp format to sync subtitles and audio.
	"""
	
	homepage = "https://k5cents.github.io/srt/"
	cran = "srt" 

	version("1.0.4", md5="f25882fca4220b8a0353153b2beae705")
	version("1.0.3", md5="801040192a33887560a83ca514113bb2")

