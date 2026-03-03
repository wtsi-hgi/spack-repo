# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAri(RPackage):
	"""Automated R Instructor

	Create videos from 'R Markdown' documents, or images and audio
    files. These images can come from image files or HTML slides, and the audio
    files can be provided by the user or computer voice narration can be created
    using 'Amazon Polly'. The purpose of this package is to allow users to create
    accessible, translatable, and reproducible lecture videos. See
    <https://aws.amazon.com/polly/> for more information.
	"""
	
	homepage = "http://github.com/seankross/ari"
	cran = "ari" 

	version("0.3.5", md5="b34b5df98cf508da75f845b859c759cd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-text2speech@0.2.8:", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("ffmpeg@3.2.4:", type=("build", "link", "run"))
