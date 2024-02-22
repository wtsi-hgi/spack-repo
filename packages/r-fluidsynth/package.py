# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFluidsynth(RPackage):
	"""Read and Play Digital Music (MIDI)

	Bindings to 'libfluidsynth' to parse and synthesize MIDI files. It can
    read MIDI into a data frame, play it on the local audio device, or convert into
    an audio file.
	"""
	
	homepage = "https://docs.ropensci.org/fluidsynth/"
	cran = "fluidsynth" 

	version("1.0.0", md5="75efd5add235c3c9698e56477a75f11a")

	depends_on("r-av", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
