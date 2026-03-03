# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsTranscribe(RPackage):
	"""Client for 'AWS Transcribe'

	Client for 'AWS Transcribe' <https://aws.amazon.com/documentation/transcribe>, a cloud transcription service that can convert an audio media file in English and other languages into a text transcript.
	"""
	
	homepage = "https://github.com/cloudyr/aws.transcribe"
	cran = "aws.transcribe" 

	version("0.1.3", md5="3b7c20fbb057156583f8dd89e0a4537f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-aws-signature@0.3.4:", type=("build", "run"))
