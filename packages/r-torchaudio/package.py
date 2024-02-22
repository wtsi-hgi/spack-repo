# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTorchaudio(RPackage):
	"""R Interface to 'pytorch''s 'torchaudio'

	Provides access to datasets, models and processing
    facilities for deep learning in audio.
	"""
	
	cran = "torchaudio" 

	version("0.3.1", md5="d88cfdef8407151b427809a986bbf45d")

	depends_on("r-torch@0.3:", type=("build", "run"))
	depends_on("r-av", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
