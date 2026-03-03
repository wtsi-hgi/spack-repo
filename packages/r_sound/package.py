# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSound(RPackage):
	"""A Sound Interface for R

	Basic functions for dealing with wav files and sound samples.
	"""
	
	homepage = "https://github.com/langenbergstefan/sound"
	cran = "sound" 

	version("1.4.6", md5="9e4942ea9ceea9563c5ab146ab4ab6ca")

	depends_on("r@2.1.14:", type=("build", "run"))
