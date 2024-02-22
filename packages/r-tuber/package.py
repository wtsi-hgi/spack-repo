# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTuber(RPackage):
	"""Client for the YouTube API

	Get comments posted on YouTube videos, information on how many 
    times a video has been liked, search for videos with particular content, and 
    much more. You can also scrape captions from a few videos. To learn more about
    the YouTube API, see <https://developers.google.com/youtube/v3/>.
	"""
	
	homepage = "http://github.com/soodoku/tuber"
	cran = "tuber" 

	version("0.9.9", md5="bef9028af580d69c25edc14e4518d4ca")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
